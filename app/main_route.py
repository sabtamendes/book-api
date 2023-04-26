from fastapi import APIRouter
from app.routes.book_route import route

route = APIRouter()

route.include_router(route, prefix="/route")
