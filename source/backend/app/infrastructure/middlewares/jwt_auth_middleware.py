import jwt
from fastapi import Request, Response, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime, timedelta

from app.core import JWT_KEY, JWT_ALGORITHM

EXCLUSION_PATH = [
    "/",
    "/favicon.ico",
    "/docs",
    "/openapi.json",
    "/api/v1/auth/signup",
    "/api/v1/auth/signin",
    "/api/v1/auth/signout",
]


class JwtAuthMiddleware(BaseHTTPMiddleware):
    """
    JWTトークンで認証するミドルウェア
    """

    async def dispatch(self, request: Request, call_next) -> Response:
        """
        ミドルウェアの処理

        Args:
            request (Request): リクエスト情報
            call_next (method): 次の処理

        Returns:
            Response: レスポンス
        """

        # JWT認証除外の場合は処理を行わない
        if request.url.path in EXCLUSION_PATH:
            return await call_next(request)

        # トークン取得
        try:
            access_token: str = request.cookies.get("access_token")
            scheme, _, token = access_token.partition(" ")
            if not access_token or scheme != "Bearer":
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="トークンが設定されていません。")
            pass
        except Exception:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="トークンが設定されていません。")

        # トークンのデコード
        try:
            payload = jwt.decode(token, JWT_KEY, algorithms=[JWT_ALGORITHM])
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="トークンの有効期限が切れています。")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="トークンが不正です。")

        # 次の処理を実行
        response: Response = await call_next(request)

        # トークンを更新
        subject: str = payload["sub"]
        payload = {
            "exp": datetime.utcnow() + timedelta(days=0, minutes=30),
            "iat": datetime.utcnow(),
            "sub": subject,
        }
        token = jwt.encode(payload, JWT_KEY, algorithm=JWT_ALGORITHM)
        response.set_cookie(key="access_token", value=f"Bearer {token}", httponly=True, samesite="none", secure=True)

        return response
