from pydantic import BaseModel
from datetime import datetime

class ResponseBookSchema(BaseModel):
    id: int
    title: str
    author: str
    professor: str
    magicCode: str
    createdAt: datetime


class RegisterBookSchema(BaseModel):
    title: str
    author: str
    professor: str 


class MagicCodeSchema(BaseModel):
    magicCode: str


class BookUpdateSchema(BaseModel):
    title: str
    author: str