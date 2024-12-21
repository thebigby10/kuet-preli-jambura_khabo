from django.db import models

from ingredient_managerapp.models import ingredient, ingredient_quantity

# Create your models here.
class recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    ingredient_quantity_id = models.ManyToManyField(ingredient_quantity)
    title = models.CharField(max_length=100)
    details = models.TextField()
    image_url = models.URLField()
    
class saved_recipe(models.Model):
    saved_recipe_id = models.AutoField(primary_key=True)
    recipe_id = models.ForeignKey(recipe, on_delete=models.CASCADE)