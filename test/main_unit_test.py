import pytest
from app.repositories.book_repositories import BookRepository
from app.schemas.book_schema import BookSchema
from app.repositories.book_repositories import BookRepository
from unittest.mock import AsyncMock

@pytest.fixture
def book_mock():
    return [
        BookSchema(id=1, title='Title', author='Author', category='category'),
        BookSchema(id=2, title='Title', author='Author', category='category')
           ]

class TestBookRepository:
    
    @pytest.mark.asyncio
    async def test_post_book(self):
        book = BookRepository()
        result = await book.post_book(1, "Title", "Author", "category")
        assert result == {
                         "id": 1, 
                          "title": "Title", 
                          "author": "Author", 
                          "category": "category"
                          }
   
    @pytest.mark.asyncio
    def test_get_all_books(self, book_mock):
        book_ = BookRepository()

        book_.get_all_books = AsyncMock(return_value=book_mock)

        books =  book_.get_all_books()
        assert isinstance(books, list)
        assert isinstance(books[0], BookSchema)




