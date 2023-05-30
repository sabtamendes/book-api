import pytest
from app.repositories.book_repositories import BookRepository
from app.schemas.book_schema import RegisterBookSchema, MagicCodeSchema
from unittest.mock import AsyncMock
from http import HTTPStatus

@pytest.fixture
def register_book_mock():
    return [
        RegisterBookSchema(id= 1, title='Title1', author='Author1', professor='Professor1', magicCode="TLCDXW", createdAt= "2023-05-29T18:10:28.871379+00:00"),
        RegisterBookSchema(id= 2, title='Title2', author='Author2', professor='Professor2', magicCode="IBWOTJ", createdAt= "2023-05-29T18:10:28.871379+00:00")
           ]

@pytest.fixture
def response_book_magicCode_mock():
    return MagicCodeSchema(magicCode="TLCDXW")


class TestBookRepository:
    # should return all books when request is successful
    @pytest.mark.asyncio
    async def test_get_all_books_success(self, register_book_mock):
        books = BookRepository()

        books.get_all_books = AsyncMock(return_value=register_book_mock)

        all_books =  await books.get_all_books()
        assert all_books == register_book_mock # igual um array de dicionários

    #should return a magicCode when the book is successfully created
    @pytest.mark.asyncio
    async def test_post_book_success(self, response_book_magicCode_mock):
        book = BookRepository()

        book.post_book = AsyncMock(return_value=response_book_magicCode_mock)

        result = await book.post_book("Title1", "Author1", "Professor1")
        assert result == response_book_magicCode_mock
    
    # should return a status code 422 when the field is blank
    @pytest.mark.asyncio
    async def test_post_book_empty_field(self):
         book = BookRepository()

         book.post_book = AsyncMock(return_value=HTTPStatus.UNPROCESSABLE_ENTITY)

         result = await book.post_book("Title1", "", "Professor1")
         assert result == HTTPStatus.UNPROCESSABLE_ENTITY

    # should return a status code 422 when the field is incorret
    @pytest.mark.asyncio
    async def test_post_book_data_diff_string(self):
        book = BookRepository()

        book.post_book = AsyncMock(return_value=HTTPStatus.UNPROCESSABLE_ENTITY)

        result = await book.post_book("Title1", 1, "Professor1")
        assert result == HTTPStatus.UNPROCESSABLE_ENTITY


   


