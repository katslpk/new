from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.about.models import CarInfo
from apps.about.models import CarPhoto
from apps.about.models import EngineType


@admin.register(CarInfo)
class CarInfoAdminModel(ModelAdmin):
    pass


@admin.register(CarPhoto)
class CarPhotoAdminModel(ModelAdmin):
    pass


@admin.register(EngineType)
class CarPhotoAdminModel(ModelAdmin):
    pass
