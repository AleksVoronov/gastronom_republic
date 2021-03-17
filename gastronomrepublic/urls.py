"""
Definition of urls for gastronomrepublic.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.hlavní, name='hlavní'),
    path('kontakty/', views.kontakty, name='kontakty'),
    path('o_nás/', views.o_nás, name='o_nás'),
    path('admin/', admin.site.urls),
]
