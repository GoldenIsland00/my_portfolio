from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class SiteSettings(models.Model):
    """Singleton-like site configuration – editable from admin."""
    site_name = models.CharField(_('نام سایت'), max_length=120, default='اسماعیل تقی‌زاده')
    site_tagline = models.CharField(_('شعار'), max_length=255, blank=True)
    logo = models.ImageField(_('لوگو'), upload_to='site/', blank=True, null=True)
    favicon = models.ImageField(_('فاوآیکون'), upload_to='site/', blank=True, null=True)
    hero_photo = models.ImageField(_('عکس پروفایل'), upload_to='site/', blank=True, null=True)
    about_text = RichTextField(_('متن درباره من'), blank=True)
    location = models.CharField(_('موقعیت'), max_length=120, blank=True, default='هرمزگان، قشم')
    status = models.CharField(_('وضعیت'), max_length=120, blank=True, default='در جستجوی پروژه جدید')
    work_type = models.CharField(_('نوع کار'), max_length=80, blank=True, default='پروژه‌ای')
    remote_note = models.CharField(_('یادداشت دورکاری'), max_length=200, blank=True)
    email = models.EmailField(_('ایمیل'), blank=True, default='sirgae.youfski@gmail.com')
    phone = models.CharField(_('تلفن'), max_length=30, blank=True, default='09925736498')
    github_url = models.URLField(_('گیت‌هاب'), blank=True)
    telegram_url = models.URLField(_('تلگرام'), blank=True)
    linkedin_url = models.URLField(_('لینکدین'), blank=True)
    default_meta_title = models.CharField(_('عنوان SEO پیش‌فرض'), max_length=70, blank=True)
    default_meta_description = models.TextField(_('توضیح SEO پیش‌فرض'), max_length=160, blank=True)
    default_meta_keywords = models.CharField(_('کلمات کلیدی SEO'), max_length=255, blank=True)
    footer_text = models.CharField(_('متن فوتر'), max_length=200, blank=True)
    is_available = models.BooleanField(_('در دسترس برای پروژه'), default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('تنظیمات سایت')
        verbose_name_plural = _('تنظیمات سایت')

    def __str__(self):
        return self.site_name or 'Site Settings'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Skill(models.Model):
    name = models.CharField(_('نام مهارت'), max_length=80)
    slug = models.SlugField(max_length=80, unique=True)
    level_percent = models.PositiveSmallIntegerField(_('درصد مهارت'), default=50)
    experience_label = models.CharField(_('برچسب تجربه'), max_length=40, blank=True)
    order = models.PositiveIntegerField(_('ترتیب'), default=0)
    is_primary = models.BooleanField(_('مهارت اصلی'), default=True)
    is_active = models.BooleanField(_('فعال'), default=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = _('مهارت فنی')
        verbose_name_plural = _('مهارت‌های فنی')

    def __str__(self):
        return self.name


class SoftSkill(models.Model):
    name = models.CharField(_('نام'), max_length=80)
    level = models.PositiveSmallIntegerField(_('سطح (۱-۵)'), default=3)
    order = models.PositiveIntegerField(_('ترتیب'), default=0)

    class Meta:
        ordering = ['order']
        verbose_name = _('مهارت نرم')
        verbose_name_plural = _('مهارت‌های نرم')

    def __str__(self):
        return self.name


class Education(models.Model):
    title = models.CharField(_('عنوان'), max_length=150)
    institution = models.CharField(_('مؤسسه'), max_length=150)
    degree = models.CharField(_('مدرک'), max_length=80, blank=True)
    start_date = models.CharField(_('شروع'), max_length=40)
    end_date = models.CharField(_('پایان'), max_length=40, blank=True, default='اکنون')
    description = models.TextField(_('توضیح'), blank=True)
    badge = models.CharField(_('نشان'), max_length=80, blank=True)
    order = models.PositiveIntegerField(_('ترتیب'), default=0)

    class Meta:
        ordering = ['order']
        verbose_name = _('تحصیلات')
        verbose_name_plural = _('تحصیلات')

    def __str__(self):
        return self.title


class Grade(models.Model):
    course = models.CharField(_('درس'), max_length=120)
    score = models.CharField(_('نمره'), max_length=10)
    context = models.CharField(_('زمینه'), max_length=150, blank=True)
    order = models.PositiveIntegerField(_('ترتیب'), default=0)

    class Meta:
        ordering = ['order']
        verbose_name = _('نمره مهم')
        verbose_name_plural = _('نمرات مهم')

    def __str__(self):
        return f'{self.course} – {self.score}'


class Certificate(models.Model):
    title = models.CharField(_('عنوان'), max_length=150)
    issuer = models.CharField(_('صادرکننده'), max_length=120)
    period = models.CharField(_('بازه'), max_length=80, blank=True)
    tags = models.CharField(_('تگ‌ها (با کاما)'), max_length=200, blank=True)
    order = models.PositiveIntegerField(_('ترتیب'), default=0)

    class Meta:
        ordering = ['order']
        verbose_name = _('گواهی')
        verbose_name_plural = _('گواهی‌ها')

    def __str__(self):
        return self.title

    def tag_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]


class Project(models.Model):
    title = models.CharField(_('عنوان'), max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    summary = models.TextField(_('خلاصه'), blank=True)
    description = RichTextField(_('توضیح کامل'), blank=True)
    status = models.CharField(_('وضعیت'), max_length=80, blank=True)
    tags = models.CharField(_('تگ‌ها (با کاما)'), max_length=255, blank=True)
    url = models.URLField(_('لینک پروژه'), blank=True)
    github_url = models.URLField(_('گیت‌هاب'), blank=True)
    image = models.ImageField(_('تصویر'), upload_to='projects/', blank=True, null=True)
    is_featured = models.BooleanField(_('ویژه'), default=True)
    is_active = models.BooleanField(_('فعال'), default=True)
    order = models.PositiveIntegerField(_('ترتیب'), default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = _('پروژه')
        verbose_name_plural = _('پروژه‌ها')

    def __str__(self):
        return self.title

    def tag_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]


class Language(models.Model):
    name = models.CharField(_('زبان'), max_length=60)
    level = models.PositiveSmallIntegerField(_('سطح (۱-۵)'), default=3)
    order = models.PositiveIntegerField(_('ترتیب'), default=0)

    class Meta:
        ordering = ['order']
        verbose_name = _('زبان')
        verbose_name_plural = _('زبان‌ها')

    def __str__(self):
        return self.name


class FavoriteTech(models.Model):
    name = models.CharField(_('تکنولوژی'), max_length=80)
    is_highlight = models.BooleanField(_('برجسته'), default=False)
    order = models.PositiveIntegerField(_('ترتیب'), default=0)

    class Meta:
        ordering = ['order']
        verbose_name = _('تکنولوژی مورد علاقه')
        verbose_name_plural = _('تکنولوژی‌های مورد علاقه')

    def __str__(self):
        return self.name


class ProjectInquiry(models.Model):
    """Contact / Start Project form submissions."""
    fullname = models.CharField(_('نام'), max_length=120)
    email = models.EmailField(_('ایمیل'))
    phone = models.CharField(_('تلفن'), max_length=30)
    company = models.CharField(_('شرکت'), max_length=120, blank=True)
    project_type = models.CharField(_('نوع پروژه'), max_length=100, blank=True)
    details = models.TextField(_('جزئیات'))
    budget = models.CharField(_('بودجه'), max_length=80, blank=True)
    timeline = models.CharField(_('بازه زمانی'), max_length=80, blank=True)
    contact_pref = models.CharField(_('روش تماس'), max_length=40, blank=True)
    extra = models.TextField(_('توضیح اضافه'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(_('خوانده شده'), default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('درخواست پروژه')
        verbose_name_plural = _('درخواست‌های پروژه')

    def __str__(self):
        return f'{self.fullname} – {self.created_at:%Y-%m-%d}'
