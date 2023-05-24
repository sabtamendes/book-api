from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int
    title: str
    author: str
    category: str

    # class Config:
    #     orm_mode = True
class RegisterBookSchema(BaseModel):
    title: str
    author: str
    category: str