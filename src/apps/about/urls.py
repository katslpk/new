from django.urls import path
from apps.about.views import IndexView
from apps.about.apps import IndexConfig

app_name = IndexConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
