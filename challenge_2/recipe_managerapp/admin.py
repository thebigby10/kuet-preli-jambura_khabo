from django.contrib import admin

from .models import recipe, saved_recipe
# Register your models here.

admin.site.register(recipe)
admin.site.register(saved_recipe)
