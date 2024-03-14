from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required

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

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            # Set the current user as the author of the recipe
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipes')  # Redirect to the recipe list page after successfully adding a recipe
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})