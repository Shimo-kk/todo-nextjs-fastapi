from fastapi import FastAPI

from app.infrastructure.middlewares.cors_middleware import CORSMiddleware
from app.infrastructure.middlewares.http_request_middleware import HttpRequestMiddleware
from app.infrastructure.middlewares.jwt_auth_middleware import JwtAuthMiddleware
from app.presentation.routers.v1 import api_v1_router

app = FastAPI()

# ミドルウェアの設定
app.add_middleware(JwtAuthMiddleware)
app.add_middleware(HttpRequestMiddleware)
app.add_middleware(CORSMiddleware)

# ルーターの設定
app.include_router(api_v1_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Hello World"}
