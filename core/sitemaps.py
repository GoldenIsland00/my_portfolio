from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Project
from blog.models import Post


class StaticSitemap(Sitemap):
    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        return ['core:home', 'blog:post_list']

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return Project.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.created_at


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.updated_at
