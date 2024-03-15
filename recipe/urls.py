from django.urls import path 
from . import views
from .views import add_recipe, edit_recipe, delete_recipe, RecipeListView

urlpatterns = [
    path('recipes/', RecipeListView.as_view(), name='recipe-list'),
    # path('', views.recipe_list, name='recipes'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('recipes/<int:recipe_id>/edit/', views.edit_recipe, name='edit_recipe'),
    path('recipes/<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),
]