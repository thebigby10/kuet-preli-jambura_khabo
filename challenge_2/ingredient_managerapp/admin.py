from django.contrib import admin

from .models import ingredient, ingredient_quantity, available_ingredient
# Register your models here.

admin.site.register(ingredient)
admin.site.register(ingredient_quantity)
admin.site.register(available_ingredient)
