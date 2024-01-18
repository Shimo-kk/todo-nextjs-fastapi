import jwt
from datetime import datetime, timedelta
from fastapi import Request, Response, HTTPException

from app.core import JWT_KEY, JWT_ALGORITHM
from app.service.usecases.auth_usecase import AuthUseCase
from app.service.models.auth_model import SignUpModel, SignInModel
from app.service.models.user_model import UserReadModel
from app.service.exceptions import (
    ValidError,
    AlreadyExistsError,
    NotFoundError,
    BadRequestError,
)


class AuthController:
    """
    認証のコントローラークラス
    """

    @staticmethod
    def sign_up(request: Request, data: SignUpModel):
        """
        サインアップ

        Args:
            request: リクエスト
            data: サインアップモデル
        """
        try:
            usecase: AuthUseCase = AuthUseCase(db_session=request.state.db_session)
            usecase.sign_up(data=data)
        except AlreadyExistsError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except ValidError as e:
            raise HTTPException(status_code=422, detail=str(e))

        return {"message": "サインアップが完了しました。"}

    @staticmethod
    def sign_in(request: Request, response: Response, data: SignInModel):
        """
        サインイン

        Args:
            request: リクエスト
            response: レスポンス
            data: サインインモデル

        Returns:
            UserReadModel: ユーザー参照モデル
        """
        try:
            usecase: AuthUseCase = AuthUseCase(db_session=request.state.db_session)
            result: UserReadModel = usecase.sign_in(data=data)

            payload = {
                "exp": datetime.utcnow() + timedelta(days=0, minutes=30),
                "iat": datetime.utcnow(),
                "sub": result.email,
            }
            token = jwt.encode(payload, JWT_KEY, algorithm=JWT_ALGORITHM)
            response.set_cookie(
                key="access_token", value=f"Bearer {token}", httponly=True, samesite="none", secure=True
            )

        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=str(e))
        except BadRequestError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception:
            raise

        return result

    @staticmethod
    def sign_out(request: Request, response: Response):
        """
        サインアウト

        Args:
            request: リクエスト
            response: レスポンス
        """
        response.set_cookie(key="access_token", value="", httponly=True, samesite="none", secure=True)
        return {"message": "サインアウトが完了しました。"}

    @staticmethod
    def get_current_signed_user(request: Request, response: Response):
        """
        現在サインインしているユーザーを取得

        Args:
            request: リクエスト
            response: レスポンス
        """
        try:
            # トークン取得
            access_token: str = request.cookies.get("access_token")
            scheme, _, token = access_token.partition(" ")
            if not access_token or scheme != "Bearer":
                raise HTTPException(status_code=401, detail="トークンが設定されていません。")

            # トークンのデコード
            try:
                payload = jwt.decode(token, JWT_KEY, algorithms=[JWT_ALGORITHM])
                subject: str = payload["sub"]
            except jwt.ExpiredSignatureError:
                raise HTTPException(status_code=401, detail="トークンの有効期限が切れています。")
            except jwt.InvalidTokenError:
                raise HTTPException(status_code=401, detail="トークンが不正です。")

            # サブジェクトを使用して、ユーザー情報を取得
            usecase: AuthUseCase = AuthUseCase(db_session=request.state.db_session)
            result: UserReadModel = usecase.get_current_signed_user(email=subject)
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=str(e))

        return result
