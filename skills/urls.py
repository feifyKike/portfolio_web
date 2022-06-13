from . import views
from django.urls import path

urlpatterns = [
    path("", views.skills_index, name="skills_index")
]