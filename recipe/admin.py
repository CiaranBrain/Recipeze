from django.contrib import admin
from .models import Category, Recipe

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',
     'ingredients', 'author', 'created_on',
      'category', 'recipe_image')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)