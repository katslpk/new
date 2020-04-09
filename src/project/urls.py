from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.urls import include


from apps.about.views import view1
from apps.education.views import view3
from apps.contact.views import view2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include("apps.contact.urls")),
    path('education/', include("apps.education.urls")),
    path('', include("apps.about.urls")),
]

