from datetime import datetime
from pydantic import BaseModel, constr


class ResponseBookSchema(BaseModel):
    id: int
    title: str
    author: str
    professor: str
    magicCode: str
    createdAt: datetime


class RegisterBookSchema(BaseModel):
    title: constr(min_length=3)
    author: constr(min_length=3)
    professor: constr(min_length=3)
   

class MagicCodeSchema(BaseModel):
    magicCode: str


class BookUpdateSchema(BaseModel):
    title: constr(min_length=3)
    author: constr(min_length=3)