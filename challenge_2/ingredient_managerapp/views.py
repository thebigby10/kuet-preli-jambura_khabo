from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView

from .serializer import IngredientSerializer, AvailableIngredientSerializer
from .models import ingredient
from rest_framework import status


# Create your views here.
class IngredientView(APIView):
    def get(self, request, ingredient_id = None):
        if ingredient_id:
            try:
                ingredient_instance = ingredient.objects.get(ingredient_id = ingredient_id)
                serializer = IngredientSerializer(ingredient_instance)
                return Response(serializer.data, status = status.HTTP_200_OK)
            except:
                return Response({"message": "ingredient not found"}, status = status.HTTP_404_NOT_FOUND)
        else:
            try:
                ingredients_instance = ingredient.objects.all()
                serializer = IngredientSerializer(ingredients_instance, many = True)
                return Response(serializer.data, status = status.HTTP_200_OK)
            except:
                return Response({"message": "ingredient not found"}, status = status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = IngredientSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "ingredient not found"}, status = status.HTTP_404_NOT_FOUND)

    def put(self, request, ingredient_id = None):
        try:
            ingredient_instance = ingredient.objects.get(ingredient_id = ingredient_id)
            serializer = IngredientSerializer(ingredient_instance, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTT_200_OK)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "ingredient not found"}, status = status.HTTP_404_NOT_FOUND)

    def delete(self, request, ingredient_id = None):
        try:
            ingredient_instance = ingredient.objects.get(ingredient_id = ingredient_id)
            ingredient_instance.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "ingredient not found"}, status = status.HTTP_404_NOT_FOUND)


class saved_ingredient_view(APIView):
    def get(self, request, ingredient_id = None):
        try:
            saved_ingredient_instance = saved_recipe.objects.get(saved_recipe_id = ingredient_id)
            serializer = AvailableIngredientSerializer(saved_ingredient_instance.recipe_id.ingredient_quantity.all(), many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except:
            return Response({"message": "ingredient not found"}, status = status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = AvailableIngredientSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "ingredient not found"}, status = status.HTTP_404_NOT_FOUND)

    def put(self, request, ingredient_id = None):
        try:
            saved_ingredient_instance = saved_recipe.objects.get(saved_recipe_id = ingredient_id)
            serializer = AllValuesFieldListFilter(saved_ingredient_instance.recipe_id.ingredient_quantity.all(), data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "ingredient not found"}, status = status.HTTP_404_NOT_FOUND)

    def delete(self, request, ingredient_id = None):
        try:
            saved_ingredient_instance = saved_recipe.objects.get(saved_recipe_id = ingredient_id)
            saved_ingredient_instance.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "ingredient not found"}, status = status.HTTP_404_NOT_FOUND)
