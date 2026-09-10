from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('set-theme/', views.set_theme, name='set_theme'),
    path('project-inquiry/', views.project_inquiry, name='project_inquiry'),
]
