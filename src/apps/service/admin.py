from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.service.models import Station
from apps.service.models import Type
from apps.service.models import Work


@admin.register(Work)
class WorkAdminModel(ModelAdmin):
    pass


@admin.register(Type)
class TypeAdminModel(ModelAdmin):
    pass


@admin.register(Station)
class StationAdminModel(ModelAdmin):
    pass
