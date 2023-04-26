# from app.schemas.common import ResponseBase
# from app.usecases.factories.sample import make_sample
from fastapi import APIRouter
from app.schemas.book_schema import (
    BookSchema
)


route = APIRouter()
