from pydantic import BaseModel


class BookSchema(BaseModel):
    title: str
    author: str
    description: str

    class Config:
        orm_mode = True
