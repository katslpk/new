from django.urls import path

from apps.contact.apps import ContactConfig
from apps.contact.views import IndexView

app_name = ContactConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
