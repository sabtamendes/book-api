# app/exceptions/base.py

from app.exceptions.exception import AppBaseException

class BookValidationException(AppBaseException):
    def __init__(self, description: str):
        super().__init__(
            status_code=400,
            context={"description": description},
        )
