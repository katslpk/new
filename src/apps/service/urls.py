from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from apps.service.apps import EducationConfig
from apps.service.views import AddWorkView
from apps.service.views import CarWorkView
from apps.service.views import WorkView

#


app_name = EducationConfig.name

urlpatterns = [
    path("", CarWorkView.as_view(), name="index"),
    path("work/", csrf_exempt(WorkView.as_view()), name="work"),
    path("add_work/", AddWorkView.as_view(), name="add_work"),
]
