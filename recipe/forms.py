from django import forms
from .models import Recipe, Comment
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


# recipe form 
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'category', 'recipe_image', 'posted']
        widgets = {
            # 'description': forms.Textarea(attrs={'rows': 4}),
            # 'ingredients': forms.Textarea(attrs={'rows': 6}),
            # 'instructions': forms.Textarea(attrs={'rows': 10}),
            'title': SummernoteWidget(),
            'description': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget(),            
        }
        
# comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
