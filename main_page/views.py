import random

from django.shortcuts import render
from .models import Category, Dish, Gallery


def main_page(request):
    categories = Category.objects.filter(is_visible=True).order_by('position')
    dishes = Dish.objects.filter(is_visible=True).order_by('position')
    special = Dish.objects.filter(is_visible=True, is_special=True).order_by('position')
    galleries = list(Gallery.objects.all())
    random.shuffle(galleries)

    return render(request, 'main.html', context={'galleries': galleries, 'categories': categories, 'dishes': dishes, 'special': special})
