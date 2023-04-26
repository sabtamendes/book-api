from fastapi import APIRouter
from app.routes.book_router import router

router = APIRouter()

router.include_router(router, prefix="/books")
