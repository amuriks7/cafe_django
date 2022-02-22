from django.contrib import admin
from .models import Category, Dish, Gallery, UserReservation

admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Gallery)
admin.site.register(UserReservation)

# Register your models here.
