from django.contrib import admin
from skills.models import Skill, ByCategory, Experience

# Register your models here.
admin.site.register(Skill)
admin.site.register(ByCategory)
admin.site.register(Experience)