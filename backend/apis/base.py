from apis.v1 import route_blogs, route_users
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_blogs.router, prefix="/blogs", tags=["blogs"])
