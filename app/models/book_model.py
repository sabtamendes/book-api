from tortoise.models import Model
from tortoise import fields

# modelo da tabela a ser construída no db
class Book(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    author = fields.CharField(max_length=255)
    category = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)

