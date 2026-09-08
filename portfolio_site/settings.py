"""
Django settings for portfolio_site – Esmaeil Taghizadeh Portfolio
"""
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-change-me-in-production-esmaeil-portfolio-2025')

DEBUG = os.environ.get('DJANGO_DEBUG', 'True').lower() in ('1', 'true', 'yes')

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'https://villiam-taghizadeh.onrender.com/,villiam-taghizadeh.onrender.com').split(',')

INSTALLED_APPS = [
    'modeltranslation',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'ckeditor',
    'ckeditor_uploader',
    'rosetta',
    'meta',
    'core.apps.CoreConfig',
    'blog.apps.BlogConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.ThemeMiddleware',
]

ROOT_URLCONF = 'portfolio_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'core.context_processors.site_settings',
                'core.context_processors.theme',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio_site.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# For production PostgreSQL, set DATABASE_URL
if os.environ.get('DATABASE_URL'):
    import dj_database_url
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------- i18n ----------
LANGUAGE_CODE = 'fa'
LANGUAGES = [
    ('fa', 'فارسی'),
    ('en', 'English'),
    ('ar', 'العربية'),  # Omani / Arabic
]
MODELTRANSLATION_DEFAULT_LANGUAGE = 'fa'
MODELTRANSLATION_LANGUAGES = ('fa', 'en', 'ar')
MODELTRANSLATION_FALLBACK_LANGUAGES = {'default': ('fa', 'en', 'ar')}

LOCALE_PATHS = [BASE_DIR / 'locale']
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ---------- Static & Media ----------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1

# ---------- CKEditor ----------
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'language': 'fa',
        'direction': 'rtl',
    },
}

# ---------- Jazzmin Admin ----------
JAZZMIN_SETTINGS = {
    'site_title': 'پنل مدیریت | اسماعیل تقی‌زاده',
    'site_header': 'Esmaeil Portfolio Admin',
    'site_brand': 'esmaeil.dev',
    'site_logo': None,
    'login_logo': None,
    'site_logo_classes': 'img-circle',
    'site_icon': None,
    'welcome_sign': 'به پنل مدیریت حرفه‌ای خوش آمدید 👋',
    'copyright': '© Esmaeil Taghizadeh — Qeshm, Iran',
    'search_model': ['blog.Post', 'core.Project', 'core.Skill'],
    'user_avatar': None,
    'topmenu_links': [
        {'name': '🏠 سایت', 'url': '/', 'new_window': True},
        {'name': '📝 وبلاگ', 'url': '/blog/', 'new_window': True},
        {'name': '⚙️ تنظیمات', 'url': '/admin/core/sitesettings/', 'new_window': False},
    ],
    'usermenu_links': [
        {'name': 'مشاهده سایت', 'url': '/', 'new_window': True, 'icon': 'fas fa-external-link-alt'},
    ],
    'show_sidebar': True,
    'navigation_expanded': True,
    'hide_apps': [],
    'hide_models': [],
    'order_with_respect_to': [
        'core',
        'core.SiteSettings',
        'core.Project',
        'core.Skill',
        'core.SoftSkill',
        'core.Education',
        'core.Certificate',
        'core.Language',
        'core.FavoriteTech',
        'core.ProjectInquiry',
        'blog',
        'blog.Post',
        'blog.Category',
        'blog.Tag',
        'auth',
    ],
    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
        'core.SiteSettings': 'fas fa-sliders-h',
        'core.Skill': 'fas fa-code',
        'core.SoftSkill': 'fas fa-handshake',
        'core.Education': 'fas fa-graduation-cap',
        'core.Grade': 'fas fa-star-half-alt',
        'core.Project': 'fas fa-project-diagram',
        'core.Certificate': 'fas fa-certificate',
        'core.Language': 'fas fa-language',
        'core.FavoriteTech': 'fas fa-heart',
        'core.ProjectInquiry': 'fas fa-envelope-open-text',
        'blog.Post': 'fas fa-newspaper',
        'blog.Category': 'fas fa-folder-open',
        'blog.Tag': 'fas fa-tags',
    },
    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fas fa-circle',
    'related_modal_active': True,
    'custom_css': 'admin/custom_admin.css',
    'custom_js': None,
    'use_google_fonts_cdn': True,
    'show_ui_builder': False,
    'changeform_format': 'horizontal_tabs',
    'changeform_format_overrides': {
        'auth.user': 'collapsible',
        'auth.group': 'vertical_tabs',
        'core.sitesettings': 'horizontal_tabs',
    },
    'language_chooser': True,
}

JAZZMIN_UI_TWEAKS = {
    'navbar_small_text': False,
    'footer_small_text': True,
    'body_small_text': False,
    'brand_small_text': False,
    'brand_colour': 'navbar-info',
    'accent': 'accent-info',
    'navbar': 'navbar-dark navbar-info',
    'no_navbar_border': True,
    'navbar_fixed': True,
    'layout_boxed': False,
    'footer_fixed': False,
    'sidebar_fixed': True,
    'sidebar': 'sidebar-dark-info',
    'sidebar_nav_small_text': False,
    'sidebar_disable_expand': False,
    'sidebar_nav_child_indent': True,
    'sidebar_nav_compact_style': False,
    'sidebar_nav_legacy_style': False,
    'sidebar_nav_flat_style': True,
    'theme': 'darkly',
    'default_theme_mode': 'dark',
    'button_classes': {
        'primary': 'btn-info',
        'secondary': 'btn-secondary',
        'info': 'btn-info',
        'warning': 'btn-warning',
        'danger': 'btn-danger',
        'success': 'btn-success',
    },
    'actions_sticky_top': True,
}

# ---------- Meta / SEO ----------
META_SITE_PROTOCOL = 'https'
META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True
META_USE_TITLE_TAG = True
META_SITE_TYPE = 'website'
META_DEFAULT_KEYWORDS = ['python', 'django', 'developer', 'portfolio', 'اسماعیل تقی‌زاده']

# ---------- Theme ----------
DEFAULT_THEME = 'dark'  # dark | light

# ---------- Email (for contact form) ----------
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@esmaeil.dev'
CONTACT_EMAIL = os.environ.get('CONTACT_EMAIL', 'sirgae.youfski@gmail.com')
