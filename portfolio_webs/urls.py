"""Defines the URL patterns for portfolio_webs"""
from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path("", views.index, name='index'),
    # About page
    path("about", views.about, name='about'),
    # Contact page
    path("contact", views.contact, name='contact'),
    # Thank you page
    path("thank_you", views.polite, name='thank_you'),
]
