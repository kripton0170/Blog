from django.contrib import admin
from .models import BlogModel, CategoryModel

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display = ['link']

@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_display_links = ['title', 'created_at']
