from django.contrib import admin
from django.shortcuts import render
from django.urls import include
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("statistic/", include("apps.statistic.urls")),
    path("service/", include("apps.service.urls")),
    path("", include("apps.about.urls")),
    path("o/", include("apps.onboarding.urls")),
    path("blog/", include("apps.blog.urls")),
    path("api/", include("apps.api.impl.v1.urls")),
]
