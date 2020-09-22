from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from apps.service.apps import EducationConfig
from apps.service.views import AddWorkView
from apps.service.views import ALLCarView
from apps.service.views import CarWorkView
from apps.service.views import StationAdd
from apps.service.views import TypeAdd
from apps.service.views import WorkDelete

app_name = EducationConfig.name

urlpatterns = [
    path("", ALLCarView.as_view(), name="index"),
    path("car/<int:pk>/work/", csrf_exempt(CarWorkView.as_view()), name="work", ),
    path(
        "car/<int:id>/work/delete/<int:pk>/",
        csrf_exempt(WorkDelete.as_view()),
        name="delete_work",
    ),
    path("add_work/", AddWorkView.as_view(), name="add_work"),
    path("add_type/", TypeAdd.as_view(), name="add_type"),
    path("add_station/", StationAdd.as_view(), name="add_station"),
]
