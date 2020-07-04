from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from apps.service.apps import EducationConfig
from apps.service.views import AddWorkView
from apps.service.views import WorkView

app_name = EducationConfig.name

urlpatterns = [
    path("", WorkView.as_view(), name="index"),
    path("add_work/", AddWorkView.as_view(), name="add_work"),
]
