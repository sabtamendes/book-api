# from app.schemas.common import ResponseBase
# from app.usecases.factories.sample import make_sample
from fastapi import APIRouter
from app.schemas.book_schema import BookSchema
from app.repositories.book_repositories import BookRepository

router = APIRouter()
book_repositories = BookRepository()

@router.get("/", status_code=200)
async def get_all_books():
    all_books = await book_repositories.get_all_books()
    return all_books
