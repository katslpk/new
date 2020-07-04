from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from apps.education.apps import EducationConfig
from apps.education.views import IndexView

app_name = EducationConfig.name

urlpatterns = [
    path("", csrf_exempt(IndexView.as_view()), name="index"),
]
