from fastapi import APIRouter

from app.presentation.routers.v1 import auth_router
from app.presentation.routers.v1 import todo_router

api_v1_router = APIRouter()
api_v1_router.include_router(auth_router.router, prefix="/auth", tags=["auth"])
api_v1_router.include_router(todo_router.router, prefix="/todo", tags=["todo"])
