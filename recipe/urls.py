from django.urls import path 
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipes'),
    path('item/', views.recipe_list, name='item')
]