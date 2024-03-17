from django.urls import path 
from . import views
from .views import add_recipe, edit_recipe, delete_recipe, RecipeListView, RecipeDetailView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:recipe_id>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('recipes/<int:recipe_id>/edit/', views.edit_recipe, name='edit_recipe'),
    path('recipes/<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),
    path('recipe/<int:recipe_id>/add_comment/', views.add_comment, name='add_comment'),
    path('recipe/<int:recipe_id>/comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('recipe/<int:recipe_id>/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('profile/', views.edit_profile, name='edit_profile'),
]