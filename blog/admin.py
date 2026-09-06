from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Category, Tag, Post


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ('title', 'category', 'status', 'is_featured', 'published_at', 'views')
    list_filter = ('status', 'is_featured', 'category')
    list_editable = ('status', 'is_featured')
    search_fields = ('title', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    date_hierarchy = 'published_at'
