from tortoise.contrib.pydantic import pydantic_model_creator
from app.models.book_model import Book
from typing import List

BookSchema = pydantic_model_creator(Book)

## essa classe é a que será expportada para o route
class BookRepository:
    @staticmethod
    async def get_all_books() -> List[BookSchema]:
        books = await Book.all().values()
        return [BookSchema.from_orm(book) for book in books]
