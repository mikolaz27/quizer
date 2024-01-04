import datetime

from django.db import models
from django.utils import timezone
from mongoengine import (DateTimeField, Document, EmbeddedDocument,
                         EmbeddedDocumentField, IntField, ListField,
                         StringField)


class Blog(EmbeddedDocument):
    name = StringField(max_length=255)
    text = StringField()
    author = StringField(max_length=255)
    rating = IntField(min_value=1, max_value=100)
    category = StringField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Entity(Document):
    blog = ListField(EmbeddedDocumentField(Blog))
    timestamp = DateTimeField(default=timezone.now())
    headline = StringField(max_length=255)

    def __str__(self):
        return f"{self.headline}"
