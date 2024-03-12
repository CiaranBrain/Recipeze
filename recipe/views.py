from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

# Create your views here.

def recipe_list(request):
    recipes = Recipe.objects.all().order_by('created_on')
    context = {'recipes': recipes}
    return render(request, './recipes_list.html', context)