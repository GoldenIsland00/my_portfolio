from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.translation import gettext as _
from django.http import JsonResponse
from .models import (
    SiteSettings, Skill, SoftSkill, Education, Grade,
    Certificate, Project, Language, FavoriteTech, ProjectInquiry
)
from blog.models import Post


def home(request):
    ctx = {
        'skills': Skill.objects.filter(is_active=True, is_primary=True),
        'extra_skills': Skill.objects.filter(is_active=True, is_primary=False),
        'soft_skills': SoftSkill.objects.all(),
        'education': Education.objects.all(),
        'grades': Grade.objects.all(),
        'certificates': Certificate.objects.all(),
        'projects': Project.objects.filter(is_active=True),
        'languages': Language.objects.all(),
        'fav_techs': FavoriteTech.objects.all(),
        'latest_posts': Post.objects.filter(status='published')[:3],
    }
    return render(request, 'core/home.html', ctx)


@require_POST
def set_theme(request):
    theme = request.POST.get('theme', 'dark')
    if theme not in ('dark', 'light'):
        theme = 'dark'
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('theme', theme, max_age=365 * 24 * 3600, samesite='Lax')
    return response


@require_POST
def project_inquiry(request):
    data = request.POST
    ProjectInquiry.objects.create(
        fullname=data.get('fullname', ''),
        email=data.get('email', ''),
        phone=data.get('phone', ''),
        company=data.get('company', ''),
        project_type=data.get('ptype', ''),
        details=data.get('details', ''),
        budget=data.get('budget', ''),
        timeline=data.get('timeline', ''),
        contact_pref=data.get('contactPref', ''),
        extra=data.get('extra', ''),
    )
    messages.success(request, _('درخواست شما ثبت شد. به زودی با شما تماس می‌گیریم.'))
    return redirect('core:home')
