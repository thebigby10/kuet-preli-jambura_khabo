from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ingredients/", include("ingredient_managerapp.urls")),
    path("recipe/ ", include("recipe_manager.urls")),
    path("ask", include("chatbot_manager.urls")),
]
