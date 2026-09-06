from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin
from .models import (
    SiteSettings, Skill, SoftSkill, Education, Grade,
    Certificate, Project, Language, FavoriteTech, ProjectInquiry
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(TranslationAdmin):
    fieldsets = (
        (_('عمومی'), {
            'fields': ('site_name', 'site_tagline', 'logo', 'favicon', 'hero_photo', 'is_available'),
            'classes': ('wide',),
        }),
        (_('درباره'), {
            'fields': ('about_text', 'location', 'status', 'work_type', 'remote_note'),
        }),
        (_('تماس'), {
            'fields': ('email', 'phone', 'github_url', 'telegram_url', 'linkedin_url'),
        }),
        (_('SEO'), {
            'fields': ('default_meta_title', 'default_meta_description', 'default_meta_keywords'),
            'classes': ('collapse',),
        }),
        (_('فوتر'), {
            'fields': ('footer_text',),
        }),
    )
    readonly_fields = ()

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Skill)
class SkillAdmin(TranslationAdmin):
    list_display = ('name', 'level_bar', 'experience_label', 'is_primary', 'order', 'is_active')
    list_editable = ('order', 'is_active', 'is_primary')
    list_filter = ('is_primary', 'is_active')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('order', 'name')

    @admin.display(description=_('درصد مهارت'))
    def level_bar(self, obj):
        color = '#0ea5e9' if obj.level_percent >= 70 else '#f59e0b' if obj.level_percent >= 40 else '#ef4444'
        return format_html(
            '<div style="background:#1e293b;border-radius:6px;width:120px;height:10px;overflow:hidden">'
            '<div style="background:{};width:{}%;height:100%;border-radius:6px"></div></div>'
            '<small style="color:#94a3b8">{}%</small>',
            color, obj.level_percent, obj.level_percent
        )


@admin.register(SoftSkill)
class SoftSkillAdmin(TranslationAdmin):
    list_display = ('name', 'level', 'stars', 'order')
    list_editable = ('level', 'order')
    ordering = ('order',)

    @admin.display(description=_('سطح'))
    def stars(self, obj):
        filled = '★' * obj.level
        empty = '☆' * (5 - obj.level)
        return format_html('<span style="color:#f59e0b;letter-spacing:2px">{}{}</span>', filled, empty)


@admin.register(Education)
class EducationAdmin(TranslationAdmin):
    list_display = ('title', 'institution', 'start_date', 'end_date', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'institution')
    ordering = ('order',)


@admin.register(Grade)
class GradeAdmin(TranslationAdmin):
    list_display = ('course', 'score', 'context', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(Certificate)
class CertificateAdmin(TranslationAdmin):
    list_display = ('title', 'issuer', 'period', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'issuer')
    ordering = ('order',)


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = ('title', 'status', 'thumb', 'is_featured', 'is_active', 'order')
    list_editable = ('is_featured', 'is_active', 'order')
    list_filter = ('is_featured', 'is_active', 'status')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'summary', 'tags')
    ordering = ('order', '-created_at')

    @admin.display(description=_('تصویر'))
    def thumb(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:40px;width:40px;object-fit:cover;border-radius:8px;border:1px solid #334155"/>',
                obj.image.url
            )
        return '—'


@admin.register(Language)
class LanguageAdmin(TranslationAdmin):
    list_display = ('name', 'level', 'order')
    list_editable = ('level', 'order')
    ordering = ('order',)


@admin.register(FavoriteTech)
class FavoriteTechAdmin(TranslationAdmin):
    list_display = ('name', 'is_highlight', 'order')
    list_editable = ('is_highlight', 'order')
    list_filter = ('is_highlight',)
    ordering = ('order',)


@admin.register(ProjectInquiry)
class ProjectInquiryAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'project_type', 'created_at', 'is_read', 'status_badge')
    list_filter = ('is_read', 'project_type', 'created_at')
    list_editable = ('is_read',)
    readonly_fields = ('created_at', 'fullname', 'email', 'phone', 'company',
                       'project_type', 'details', 'budget', 'timeline',
                       'contact_pref', 'extra')
    search_fields = ('fullname', 'email', 'details', 'company')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

    @admin.display(description=_('وضعیت'))
    def status_badge(self, obj):
        if obj.is_read:
            return format_html(
                '<span style="background:#10b98133;color:#10b981;padding:3px 10px;'
                'border-radius:20px;font-size:12px;font-weight:600">خوانده‌شده</span>'
            )
        return format_html(
            '<span style="background:#f59e0b33;color:#f59e0b;padding:3px 10px;'
            'border-radius:20px;font-size:12px;font-weight:600">جدید</span>'
        )

    def has_add_permission(self, request):
        return False
