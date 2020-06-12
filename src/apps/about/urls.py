from django.urls import path

from apps.about.apps import IndexConfig
from apps.about.views import CarInfoView

app_name = IndexConfig.name

urlpatterns = [
    path("", CarInfoView.as_view(), name="index"),
]
