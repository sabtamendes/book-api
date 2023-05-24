from tortoise import fields
from tortoise.models import Model


class Book(Model):
    id = fields.IntField(pk=True, generated=True)
    title = fields.CharField(max_length=255)
    author = fields.CharField(max_length=255)
    category = fields.CharField(max_length=255)
    # created_at = fields.DatetimeField(auto_now_add=True)
    class Meta:
        table = "Book"