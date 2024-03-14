from django.urls import path 
from . import views
from .views import add_recipe

urlpatterns = [
    path('', views.recipe_list, name='recipes'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('add_recipe/', add_recipe, name='add_recipe'),
]