# اسماعیل تقی‌زاده — پورتفولیو Django

وب‌سایت پورتفولیو سه‌زبانه (فارسی / انگلیسی / عربی عمانی) با تم دارک و لایت، وبلاگ، پنل مدیریت حرفه‌ای (Jazzmin) و SEO کامل.

## ویژگی‌ها

- **سه‌زبانه**: فارسی (پیش‌فرض)، انگلیسی، عربی — با `django-modeltranslation` + `LocaleMiddleware`
- **دو تم**: Dark / Light با ذخیره در Cookie
- **وبلاگ**: پست، دسته، تگ، SEO meta برای هر پست
- **پنل ادمین حرفه‌ای**: Jazzmin + ترجمه محتوا + CKEditor
- **سفارشی‌سازی کامل**: تنظیمات سایت، مهارت‌ها، تحصیلات، پروژه‌ها، گواهی‌ها از ادمین
- **SEO**: meta tags، Open Graph، Twitter Cards، JSON-LD، Sitemap.xml
- **فرم شروع پروژه**: چندمرحله‌ای (wizard) با ذخیره در دیتابیس
- **آماده Deploy**: WhiteNoise، پشتیبانی PostgreSQL، Gunicorn

## نصب سریع (لوکال)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- سایت: http://127.0.0.1:8000/
- ادمین: http://127.0.0.1:8000/admin/  (کاربر پیش‌فرض در صورت seed: `admin` / `admin123`)

## تغییر زبان

از منوی بالای صفحه یا پیشوند URL: `/en/` ، `/ar/`

## تغییر تم

دکمه ☀/☾ در هدر — در Cookie ذخیره می‌شود.

## Deploy (مثال با Gunicorn + Nginx)

```bash
pip install gunicorn
export DJANGO_DEBUG=False
export DJANGO_SECRET_KEY='your-secret'
export DJANGO_ALLOWED_HOSTS='yourdomain.com'
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn portfolio_site.wsgi:application --bind 0.0.0.0:8000
```

برای PostgreSQL:

```bash
pip install psycopg2-binary dj-database-url
export DATABASE_URL=postgres://user:pass@host:5432/dbname
```

## ساختار

```
portfolio_site/
├── core/          # پورتفولیو، تنظیمات سایت، فرم تماس
├── blog/          # وبلاگ
├── templates/     # قالب‌ها
├── static/        # CSS / JS
├── locale/        # ترجمه‌های gettext (اختیاری)
└── portfolio_site/  # settings, urls
```

## نکات SEO

- `sitemap.xml` در ریشه
- JSON-LD Person schema در base
- meta title/description قابل تنظیم از ادمین برای سایت و هر پست
- `hreflang` از طریق i18n_patterns

