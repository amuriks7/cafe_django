from django.db import models
from uuid import uuid4
from os import path


class Category(models.Model):
    name = models.CharField(max_length=40, unique=True, db_index=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        ordering = ('position', )


class Dish(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/dishes', filename)

    name = models.CharField(max_length=50, unique=True, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.TextField(max_length=500, blank=True)
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    position = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.name}: {self.price}'


class Gallery(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/gallery', filename)

    name = models.CharField(max_length=40, unique=True)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return self.name
