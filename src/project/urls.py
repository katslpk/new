from django.contrib import admin
from django.shortcuts import render
from django.urls import include
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("contact/", include("apps.contact.urls")),
    path("education/", include("apps.education.urls")),
    path("", include("apps.about.urls")),
    path("o/", include("apps.onboarding.urls")),
]
