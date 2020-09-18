from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.about.models import CarInfo
from apps.about.models import CarPhoto


@admin.register(CarInfo)
class CarInfoAdminModel(ModelAdmin):
    pass


@admin.register(CarPhoto)
class CarPhotoAdminModel(ModelAdmin):
    pass
