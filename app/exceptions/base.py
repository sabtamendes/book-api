# app/exceptions/base.py

from app.exceptions.exception import AppBaseException

class BookValidationException(AppBaseException):
    def __init__(self, category: str):
        super().__init__(
            status_code=404,
            context={"category": category},
        )
