from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.about.models import CarInfo, CarPhoto


@admin.register(CarInfo)
class CarInfoAdminModel(ModelAdmin):
    pass

@admin.register(CarPhoto)
class CarPhotoAdminModel(ModelAdmin):
    pass