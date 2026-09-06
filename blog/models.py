from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from meta.models import ModelMeta


class Category(models.Model):
    name = models.CharField(_('نام'), max_length=80)
    slug = models.SlugField(max_length=80, unique=True)
    description = models.TextField(_('توضیح'), blank=True)

    class Meta:
        verbose_name = _('دسته‌بندی')
        verbose_name_plural = _('دسته‌بندی‌ها')
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})


class Tag(models.Model):
    name = models.CharField(_('نام'), max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = _('تگ')
        verbose_name_plural = _('تگ‌ها')
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(ModelMeta, models.Model):
    STATUS_CHOICES = (
        ('draft', _('پیش‌نویس')),
        ('published', _('منتشر شده')),
    )
    title = models.CharField(_('عنوان'), max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(_('خلاصه'), max_length=300, blank=True)
    body = RichTextField(_('متن'))
    cover = models.ImageField(_('تصویر کاور'), upload_to='blog/', blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='posts', verbose_name=_('دسته‌بندی')
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name=_('تگ‌ها'))
    status = models.CharField(_('وضعیت'), max_length=12, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(_('ویژه'), default=False)
    meta_title = models.CharField(_('عنوان SEO'), max_length=70, blank=True)
    meta_description = models.TextField(_('توضیح SEO'), max_length=160, blank=True)
    meta_keywords = models.CharField(_('کلمات کلیدی'), max_length=255, blank=True)
    published_at = models.DateTimeField(_('تاریخ انتشار'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(_('بازدید'), default=0)

    _metadata = {
        'title': 'get_meta_title',
        'description': 'get_meta_description',
        'keywords': 'get_meta_keywords',
        'image': 'get_meta_image',
    }

    class Meta:
        ordering = ['-published_at', '-created_at']
        verbose_name = _('پست')
        verbose_name_plural = _('پست‌ها')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    def get_meta_title(self):
        return self.meta_title or self.title

    def get_meta_description(self):
        return self.meta_description or self.excerpt

    def get_meta_keywords(self):
        if self.meta_keywords:
            return [k.strip() for k in self.meta_keywords.split(',')]
        return [t.name for t in self.tags.all()]

    def get_meta_image(self):
        if self.cover:
            return self.cover.url
        return None
