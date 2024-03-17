from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django import forms
from django_summernote.fields import SummernoteTextField

from django.db.models.signals import post_save
from django.dispatch import receiver


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

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', default='static/images/nobodyc.jpg')
    favourite_food = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return str(self.user.username)
