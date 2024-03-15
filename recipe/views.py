from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Recipe, Comment
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView

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

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'
    context_object_name = 'recipes'
    paginate_by = 9

    def get_queryset(self):
        return Recipe.objects.filter(posted=1).order_by('created_on')


# def recipe_list(request):
#     recipes = Recipe.objects.filter(posted=1).order_by('created_on')
#     context = {'recipes': recipes}
#     return render(request, 'recipes_list.html', context)

# def recipe_detail(request, recipe_id):
#     recipe = get_object_or_404(Recipe, pk=recipe_id)
#     return render(request, 'recipe_detail.html', {'recipe': recipe})

@login_required
def add_comment(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        Comment.objects.create(author=request.user, recipe=recipe, comment = comment_text)
        return redirect('recipe_detail', recipe_id=recipe.id)
    return render(request, 'add_comment.html')

@login_required
def edit_comment(request, recipe_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, recipe_id=recipe_id, author=request.user)
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            comment.comment = comment_text
            comment.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    return render(request, 'edit_comment.html', {'comment': comment})

@login_required
def delete_comment(request, recipe_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, recipe_id=recipe_id, author=request.user)
    if request.method == 'POST':
        comment.delete()
        return redirect('recipe_detail', recipe_id=recipe.id)
    return render(request, 'delete_comment.html', {'comment': comment})

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    context_object_name = 'recipe'

    def get_object(self):
        recipe_id = self.kwargs.get("recipe_id")
        return get_object_or_404(Recipe, pk=recipe_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(recipe=self.get_object()).order_by('-created_on')
        return context




@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            # Set the current user as the author of the recipe
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe-list')  # Redirect to the recipe list page after successfully adding a recipe
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})

@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=recipe.id)# Redirect to the recipe detail page after successfully editing a recipe
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'edit_recipe.html', {'form': form})

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes')
    return render(request, 'delete_recipe.html', {'recipe': recipe})