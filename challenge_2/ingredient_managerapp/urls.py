from django.urls import path
from .views import IngredientView, saved_ingredient_view

urlpatterns = [
    path('', IngredientView.as_view()),  # List all ingredients / Create a new ingredient
    path('<int:ingredient_id>', IngredientView.as_view()),  # Get/Update/Delete a specific ingredient
    path('saved', saved_ingredient_view.as_view()),
]

