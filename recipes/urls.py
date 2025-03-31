from django.urls import path
from .views import add_recipe, recipe_list, recipe_details

urlpatterns = [
    path('add/', add_recipe, name='add_recipe'),
    path('', recipe_list, name='recipe_list'),
    path('<int:recipe_id>/', recipe_details, name='recipe_details')
]
