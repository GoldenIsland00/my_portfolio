from modeltranslation.translator import translator, TranslationOptions
from .models import (
    SiteSettings, Skill, SoftSkill, Education, Grade,
    Certificate, Project, Language, FavoriteTech, Testimonial
)


class SiteSettingsTranslation(TranslationOptions):
    fields = (
        'site_name', 'site_tagline', 'about_text', 'location',
        'status', 'work_type', 'remote_note', 'default_meta_title',
        'default_meta_description', 'default_meta_keywords', 'footer_text',
    )


class SkillTranslation(TranslationOptions):
    fields = ('name', 'experience_label')


class SoftSkillTranslation(TranslationOptions):
    fields = ('name',)


class EducationTranslation(TranslationOptions):
    fields = ('title', 'institution', 'degree', 'start_date', 'end_date', 'description', 'badge')


class GradeTranslation(TranslationOptions):
    fields = ('course', 'context')


class CertificateTranslation(TranslationOptions):
    fields = ('title', 'issuer', 'period', 'tags')


class ProjectTranslation(TranslationOptions):
    fields = ('title', 'summary', 'description', 'status', 'tags')


class LanguageTranslation(TranslationOptions):
    fields = ('name',)


class FavoriteTechTranslation(TranslationOptions):
    fields = ('name',)


class TestimonialTranslation(TranslationOptions):
    fields = ('name', 'project_topic', 'comment')


translator.register(SiteSettings, SiteSettingsTranslation)
translator.register(Skill, SkillTranslation)
translator.register(SoftSkill, SoftSkillTranslation)
translator.register(Education, EducationTranslation)
translator.register(Grade, GradeTranslation)
translator.register(Certificate, CertificateTranslation)
translator.register(Project, ProjectTranslation)
translator.register(Language, LanguageTranslation)
translator.register(FavoriteTech, FavoriteTechTranslation)
translator.register(Testimonial, TestimonialTranslation)
