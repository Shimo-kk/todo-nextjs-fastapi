from fastapi import APIRouter
from app.presentation.routers.v1 import auth_router

api_v1_router = APIRouter()
api_v1_router.include_router(auth_router.router, prefix="/auth", tags=["auth"])
