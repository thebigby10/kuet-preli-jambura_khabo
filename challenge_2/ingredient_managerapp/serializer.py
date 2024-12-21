from rest_framework import serializers
from .models import ingredient, ingredient_quantity, available_ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ingredient
        fields = ['ingredient_id', 'name', 'description']
        
class IngredientQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ingredient_quantity
        fields = ['ingredient_quantity_id', 'ingredient_id', 'quantity']

class AvailableIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = available_ingredient
        fields = ['available_ingredient_id', 'ingredient_quantity']

