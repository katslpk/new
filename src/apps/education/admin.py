from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.education.models import Project, Technology


@admin.register(Project)
class ProjectInfoAdminModel(ModelAdmin):
    pass


@admin.register(Technology)
class TechnologyAdminModel(ModelAdmin):
    pass