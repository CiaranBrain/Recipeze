from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Recipe, Comment


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'description',
     'ingredients', 'instructions', 'author', 'created_on',
      'category', 'recipe_image')
    summernote_fields = 'ingredients', 'instructions'
    list_filter = ('posted',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment,)