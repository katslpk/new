from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.api.impl.v1.views import WorkViewSet

router = DefaultRouter()
router.register("work", WorkViewSet, "work")

urlpatterns = [
    path("", include(router.urls)),
]
