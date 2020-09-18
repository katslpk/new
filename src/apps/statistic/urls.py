from django.urls import path

from apps.statistic.apps import StatisticConfig
from apps.statistic.views import IndexView

app_name = StatisticConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
