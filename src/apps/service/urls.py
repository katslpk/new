from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from apps.service.apps import EducationConfig
from apps.service.views import AddWorkView
from apps.service.views import ALLCarView
from apps.service.views import CarWorkView

app_name = EducationConfig.name

urlpatterns = [
    path("", ALLCarView.as_view(), name="index"),
    path("car/<int:pk>/work/", csrf_exempt(CarWorkView.as_view()), name="work",),
    path("add_work/", AddWorkView.as_view(), name="add_work"),
]
