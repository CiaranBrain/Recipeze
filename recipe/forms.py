from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'category', 'recipe_image', 'posted']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'ingredients': forms.Textarea(attrs={'rows': 6}),
            'instructions': forms.Textarea(attrs={'rows': 10}),
        }