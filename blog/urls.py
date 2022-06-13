"""URL's for the blog application"""
from django.urls import path
from . import views

urlpatterns = [
    # Blog page
    path("", views.blog_index, name='blog_index'),
    path("<int:pk>/", views.blog_detail, name='blog_detail'),
]
