from django.conf import settings
from .models import SiteSettings


def site_settings(request):
    return {'site': SiteSettings.load()}


def theme(request):
    return {
        'theme': getattr(request, 'theme', getattr(settings, 'DEFAULT_THEME', 'dark')),
        'LANGUAGES': settings.LANGUAGES,
    }
