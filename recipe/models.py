from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django import forms
from django_summernote.fields import SummernoteTextField


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    recipe_image = CloudinaryField('image', default='placeholder')
    posted = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'category', 'recipe_image', 'posted']


class Comment(models.Model):
    """
    Stores a single comment entry 
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.comment} by {self.author}"


    