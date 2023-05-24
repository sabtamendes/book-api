from app.models.book_model import Book
from tortoise.exceptions import DoesNotExist
from typing import List
from app.schemas.book_schema import MagicCodeSchema
import random
import string




class BookRepository:
    def generate_unique_code(self, length=6):
        letters = string.ascii_uppercase
        code = ''.join(random.sample(letters, length))
        return code
    


    async def get_all_books(self) -> List[Book]:
        return await Book.all()
    
    
    async def post_book(self, title, author, professor) -> MagicCodeSchema:
        magicCode = self.generate_unique_code()
        response = await Book.create(author=author, title=title, professor=professor, magicCode=magicCode)
        return {"magicCode": response.magicCode}


    async def get_book_by_id(self, id: int) -> Book:
        return await Book.get(id=id)




