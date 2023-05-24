from app.models.book_model import Book
from typing import List
from app.schemas.book_schema import RegisterBookSchema


class BookRepository:
    def get_all_books(self) -> List[Book]:
        # return [
        #     {
        #         "id": 1,
        #         "title": "A lua em Marte",
        #         "author": "Autor A",
        #         "category": "Um livro emocionante sobre a exploração lunar em Marte."
        #     },
        #     {
        #         "id": 2,
        #         "title": "O segredo do sucesso",
        #         "author": "Autor B",
        #         "category": "Um guia prático para alcançar o sucesso em todas as áreas da vida."
        #     }
        # ]

        return Book.all()
    

    async def post_book(self, title, author, category):
        #  return {
        #      "id": id,
        #      "title": title,
        #      "author": author,
        #      "category": category
        #  }
        # book = RegisterBookSchema(author=author, title=title, category=category)
        return await Book.create(author=author, title=title, category=category)

