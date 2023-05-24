from fastapi import APIRouter, HTTPException
from app.schemas.book_schema import BookSchema, RegisterBookSchema, GetBookSchema, MagicCodeSchema
from app.repositories.book_repositories import BookRepository
from typing import List
router = APIRouter()
book_repositories = BookRepository()

@router.get("/books", status_code=200, response_model=List[GetBookSchema]) #response lista de dicionários
async def get_all_books():
    all_books = await book_repositories.get_all_books()
    return all_books

# @router.get("/hello/{name}")
# async def read_hello(name: str):
#     return {"message": f"Hello {name}"}

@router.get("/health/")
async def read_health():
    return {"message": "Hello Sabta"}


@router.post("/book", status_code=201, response_model=MagicCodeSchema)
async def post_book(book: RegisterBookSchema):
    response = await book_repositories.post_book(book.title, book.author, book.professor, book.magicCode) #passando parametro
    return response


# path params
@router.get("/book/{book_id}")
async def get_book_by_id(book_id: int):
    return {"book": book_id}

#query params
@router.get("/author/")
async def get_author_by_query(author: str):
    return {"author": author}