from django.urls import path

from apps.about.apps import IndexConfig
from apps.about.views import IndexView

app_name = IndexConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
