from django.urls import path

from apps.about.apps import IndexConfig
from apps.about.views import CarAdd
from apps.about.views import CarInfoView

app_name = IndexConfig.name

urlpatterns = [
    path("", CarInfoView.as_view(), name="index"),
    path("add_car/", CarAdd.as_view(), name="car_add"),
]
