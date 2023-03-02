from django.db import models
from pydantic import BaseModel


class Product(models.Model):
    article = models.CharField(max_length=20)
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.brand} - {self.title}"


class ParsingResult(BaseModel):
    article: int
    brand: str
    title: str

