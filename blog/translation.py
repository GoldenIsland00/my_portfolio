from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Tag, Post


class CategoryTranslation(TranslationOptions):
    fields = ('name', 'description')


class TagTranslation(TranslationOptions):
    fields = ('name',)


class PostTranslation(TranslationOptions):
    fields = ('title', 'excerpt', 'body', 'meta_title', 'meta_description', 'meta_keywords')


translator.register(Category, CategoryTranslation)
translator.register(Tag, TagTranslation)
translator.register(Post, PostTranslation)
