from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe

# Create your views here.

# def recipe_list(request):
#     recipes = Recipe.objects.all().order_by('created_on')
#     context = {'recipes': recipes}
#     return render(request, './recipes_list.html', context)

# # def recipe_detail(request, pk):
# #     recipe_object = Recipe.objects.all()
# #     recipes = get_object_or_404(Recipe, pk=pk)
# #     context = {'recipes': recipes}
# #     return render(request, './recipe_detail.html', context)

# def recipe_detail(request, pk):
#     single_recipes = get_object_or_404(Recipe, pk=pk)
#     context = {'single_recipe': single_recipe}
#     return render(request, 'recipe_detail.html', context)


    # new

def recipe_list(request):
    recipes = Recipe.objects.all().order_by('created_on')
    context = {'recipes': recipes}
    return render(request, 'recipes_list.html', context)

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})