from django.shortcuts import render
from skills.models import Skill, ByCategory, Experience

# Create your views here.
def skills_index(request):
    skills = Skill.objects.all()
    bycategories = ByCategory.objects.all()
    experiences = Experience.objects.all()
    context = {
        'skills': skills,
        'bycategories': bycategories,
        'experiences': experiences
    }
    return render(request, 'skills/skills_index.html', context)