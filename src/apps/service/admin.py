from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.service.models import Work


@admin.register(Work)
class WorkAdminModel(ModelAdmin):
    pass
