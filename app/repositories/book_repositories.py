from app.models.book_model import Book
from app.schemas.book_schema import MagicCodeSchema, BookUpdateSchema
from fastapi import HTTPException
import random
import string
from typing import List
from tortoise.exceptions import DoesNotExist


class BookRepository:
    def generate_unique_code(self, length=6):
        letters = string.ascii_uppercase
        code = ''.join(random.sample(letters, length))
        return code
    

    async def get_all_books(self) -> List[Book]:
        response = await Book.all()
        return response
    
    
    async def post_book(self, title, author, professor) -> MagicCodeSchema:
        magicCode = self.generate_unique_code()
        response = await Book.create(author=author, title=title, professor=professor, magicCode=magicCode)
        return {"magicCode": response.magicCode}


    async def get_book_by_id(self, id: int) -> Book:
        try:
            response = await Book.get(id=id)
            return response
        except DoesNotExist:
<<<<<<< HEAD
            raise HTTPException(status_code=404, detail="Book not found")
=======
            raise HTTPException(status_code=404, detail="Not Found")
>>>>>>> c63b13b (feat: alteração)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))



    async def get_book_by_magicCode(self, magicCode: str) -> Book:
        return await Book.get(magicCode=magicCode)


    async def update_book(self, id: int, book_data: BookUpdateSchema):
        book = await Book.get(id=id)
        if book:
            book.title = book_data.title
            book.author = book_data.author
            await book.save()
            return {"message": "Livro atualizado com sucesso."}
        else:
            return {"message": "Livro não encontrado."}


    async def delete_book(self, id: int):
        book = await Book.get(id=id)

        await book.delete()

    @staticmethod
    async def get_ordered_books():
        query = Book.all().order_by('id')
        books = await query
        return books


