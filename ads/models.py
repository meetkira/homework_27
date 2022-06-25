from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class Ad(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True)
    address = models.CharField(max_length=250)
    is_published = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=50)
