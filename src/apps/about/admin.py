from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.about.models import CarInfo


@admin.register(CarInfo)
class CarInfoAdminModel(ModelAdmin):
    pass
