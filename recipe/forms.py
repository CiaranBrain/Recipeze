from django import forms
from .models import Recipe, Comment
from cloudinary.models import CloudinaryField
from cloudinary.forms import CloudinaryFileField
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class RecipeForm(forms.ModelForm):
    """Form for creating and editing recipes with
    rich text editing for ingredients and instructions."""

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions',
                  'category', 'recipe_image', 'posted']
        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget(),
        }


class CommentForm(forms.ModelForm):
    """Simple form for users to submit comments."""

    class Meta:
        model = Comment
        fields = ('comment',)
