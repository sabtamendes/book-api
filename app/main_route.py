from fastapi import APIRouter
from app.routes.book_router import router 

route = APIRouter()

route.include_router(router, prefix="/api")
