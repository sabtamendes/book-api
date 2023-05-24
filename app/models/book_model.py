from tortoise import fields
from tortoise.models import Model
from datetime import datetime

class Book(Model):
    id = fields.IntField(pk=True, generated=True) #é criado automaticamente
    title = fields.CharField(max_length=255)
    author = fields.CharField(max_length=255)
    professor = fields.CharField(max_length=255)
    magicCode = fields.CharField(min_legth=6, max_length=6, unique=True)
    createdAt = fields.DatetimeField(auto_now_add=True, default=datetime.now) #é criado automaticamente

    class Meta:
        table = "Book"
