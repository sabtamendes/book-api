from pydantic import BaseModel
from datetime import datetime

class GetBookSchema(BaseModel):
    id: int
    title: str
    author: str
    professor: str
    magicCode: str
    createdAt: datetime

class BookSchema(BaseModel):
    id: int
    title: str
    author: str
    category: str


class RegisterBookSchema(BaseModel):
    title: str
    author: str
    professor: str
    magicCode: str

class MagicCodeSchema(BaseModel):
    magicCode: str