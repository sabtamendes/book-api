from fastapi import APIRouter, Body
from app.schemas.book_schema import  RegisterBookSchema, ResponseBookSchema, MagicCodeSchema, BookUpdateSchema
from app.repositories.book_repositories import BookRepository
from typing import List


router = APIRouter()
book_repositories = BookRepository()


@router.get("/health")
async def read_health():
    return {"message": "Hello World"}


@router.get("/book", status_code=200, response_model=List[ResponseBookSchema]) #response lista de dicionários
async def get_all_books():
    all_books = await book_repositories.get_all_books()
    return all_books


@router.post("/book", status_code=201, response_model=MagicCodeSchema)
async def post_book(book: RegisterBookSchema):
    response = await book_repositories.post_book(book.title, book.author, book.professor) #passando parametro
    return response


# path params
@router.get("/book/{id}", status_code=200, response_model=ResponseBookSchema)
async def get_book_by_id(id: int):
    response = await book_repositories.get_book_by_id(id)
    return response

# query params
@router.get("/book/", status_code=200, response_model=ResponseBookSchema)
async def get_book_by_magicCode(magicCode: str):
    response = await book_repositories.get_book_by_magicCode(magicCode)
    return response

@router.put("/books/{id}") # path  params
async def update_book(id: int, book_data: BookUpdateSchema): #requisição por body
    response = await book_repositories.update_book(id, book_data)
    return response

@router.delete("/book/{book_id}", status_code=204)
async def delete_book(book_id: int):
    await book_repositories.delete_book(book_id)

@router.get("/ordenado")
async def get_ordered_books():
    response = await book_repositories.get_ordered_books()
    return response