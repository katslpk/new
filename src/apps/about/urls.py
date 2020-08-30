from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from apps.about.apps import IndexConfig
from apps.about.views import ALLCarInfoView
from apps.about.views import CarAdd
from apps.about.views import CarInfoDelete
from apps.about.views import CarInfoView
from apps.service.views import WorkView

app_name = IndexConfig.name

urlpatterns = [
    path("", ALLCarInfoView.as_view(), name="index"),
    path("car/<int:pk>/", csrf_exempt(CarInfoView.as_view()), name="index_car"),
    path(
        "car/<int:pk>/delete/",
        csrf_exempt(CarInfoDelete.as_view()),
        name="index_delete",
    ),
    path("add_car/", CarAdd.as_view(), name="car_add"),
]
