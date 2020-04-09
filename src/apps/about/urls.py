from django.urls import path
from apps.about.views import view1
from apps.about.apps import IndexConfig

app_name = IndexConfig.name

urlpatterns = [
    path('', view1, name = "index"),
]