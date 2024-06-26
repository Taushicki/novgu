"""Database models"""

from tortoise.models import Model
from tortoise import fields


class Student(Model):
    id = fields.IntField(pk=True)
    manid = fields.IntField()
    COURCE = fields.CharField(max_length=255)
    GRP_NAME = fields.CharField(max_length=255)
    FS_NAME = fields.CharField(max_length=255)
    NAME = fields.CharField(max_length=255)
    SURNAME = fields.CharField(max_length=255)
    PATRON = fields.CharField(max_length=255)
    SPE_SHIFR = fields.CharField(max_length=255)
    SPEC_NAME = fields.CharField(max_length=255)
