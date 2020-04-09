from django.urls import path
from apps.education.views import view3
from apps.education.apps import EducationConfig

app_name = EducationConfig.name

urlpatterns = [
    path('', view3, name = "index"),
]