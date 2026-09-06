from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import F
from .models import Post, Category, Tag


def post_list(request):
    qs = Post.objects.filter(status='published')
    category_slug = request.GET.get('category')
    tag_slug = request.GET.get('tag')
    if category_slug:
        qs = qs.filter(category__slug=category_slug)
    if tag_slug:
        qs = qs.filter(tags__slug=tag_slug)
    paginator = Paginator(qs, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    Post.objects.filter(pk=post.pk).update(views=F('views') + 1)
    post.refresh_from_db()
    related = Post.objects.filter(status='published', category=post.category).exclude(pk=post.pk)[:3]
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'related': related,
    })


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    qs = Post.objects.filter(status='published', category=category)
    paginator = Paginator(qs, 9)
    posts = paginator.get_page(request.GET.get('page'))
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'category': category,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
    })
