from app.models.book_model import Book
from typing import List
from app.schemas.book_schema import MagicCodeSchema


class BookRepository:
    async def get_all_books(self) -> List[Book]:
        return await Book.all()
    

    async def post_book(self, title, author, professor, magicCode) -> MagicCodeSchema:
           magicCode = await Book.create(author=author, title=title, professor=professor, magicCode=magicCode)
           return {"magicCode": magicCode.magicCode}


