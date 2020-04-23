from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.education.models import Degree, Education, Skills


@admin.register(Degree)
class DegreeInfoAdminModel(ModelAdmin):
    pass


@admin.register(Education)
class EducationAdminModel(ModelAdmin):
    pass


@admin.register(Skills)
class SkillsAdminModel(ModelAdmin):
    pass
