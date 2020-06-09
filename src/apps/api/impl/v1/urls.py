from django.urls import include
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter

from apps.api.impl.v1.views import TelegramView
from apps.api.impl.v1.views import WorkViewSet

router = DefaultRouter()
router.register("work", WorkViewSet, "work")

urlpatterns = [
    path("", include(router.urls)),
    path("tg/", csrf_exempt(TelegramView.as_view())),
]
