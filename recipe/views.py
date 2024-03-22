from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib import messages

import cloudinary.uploader


# Recipe List View for a list view in html
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'
    context_object_name = 'recipes'
    paginate_by = 9

    def get_queryset(self):
        return Recipe.objects.filter(posted=1).order_by('-created_on')


# comment section
@login_required
def add_comment(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        Comment.objects.create(author=request.user, recipe=recipe,
                               comment=comment_text)
        messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted'
        )
        return redirect('recipe_detail', recipe_id=recipe.id)
    return render(request, 'add_comment.html')


@login_required
def edit_comment(request, recipe_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, recipe_id=recipe_id,
                                author=request.user)
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            comment.comment = comment_text
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment Modified'
            )
            return redirect('recipe_detail', recipe_id=recipe.id)
    return render(request, 'edit_comment.html', {'comment': comment})


@login_required
def delete_comment(request, recipe_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, recipe_id=recipe_id,
                                author=request.user)
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        comment.delete()
        messages.add_message(
                request, messages.SUCCESS,
                'Comment Deleted'
            )
        return redirect('recipe_detail', recipe_id=recipe.id)
    return render(request, 'delete_comment.html', {'comment': comment})


# Detailed Recipe view
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    context_object_name = 'recipe'

    def get_object(self):
        recipe_id = self.kwargs.get("recipe_id")
        return get_object_or_404(Recipe, pk=recipe_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            recipe=self.get_object()).order_by('-created_on')
        return context


# Add edit or delete recipe
@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Recipe Posted'
            )
            return redirect('recipe-list')
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
            messages.add_message(
                request, messages.SUCCESS,
                'Recipe Modified'
            )
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'edit_recipe.html', {'form': form})


@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        recipe.delete()
        messages.add_message(
                request, messages.SUCCESS,
                'Recipe Deleted'
            )
        return redirect('recipe-list')
    return render(request, 'delete_recipe.html', {'recipe': recipe})
