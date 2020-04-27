from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.education.models import Station, Work


@admin.register(Station)
class StationInfoAdminModel(ModelAdmin):
    pass


@admin.register(Work)
class WorkAdminModel(ModelAdmin):
    pass


