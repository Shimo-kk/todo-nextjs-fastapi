from fastapi import FastAPI

from app.infrastructure.middlewares.cors_middleware import CORSMiddleware
from app.infrastructure.middlewares.http_request_middleware import HttpRequestMiddleware

app = FastAPI()

# ミドルウェアの設定
app.add_middleware(HttpRequestMiddleware)
app.add_middleware(CORSMiddleware)


@app.get("/")
async def root():
    return {"message": "Hello World"}
