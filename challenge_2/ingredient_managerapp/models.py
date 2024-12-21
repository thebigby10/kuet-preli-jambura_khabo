from django.db import models

# Create your models here.
class ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
   
class ingredient_quantity(models.Model):
    ingredient_quantity_id = models.AutoField(primary_key=True)
    ingredient_id = models.ForeignKey(ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.ingredient_id.name + " : " + str(self.quantity)


class available_ingredient(models.Model):
    available_ingredient_id = models.ForeignKey(ingredient, on_delete=models.CASCADE)
    ingredient_quantity = models.ManyToManyField(ingredient_quantity)
    
    def __str__(self):
        return self.available_ingredient_id.name
    
