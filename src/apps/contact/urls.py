from django.urls import path
from apps.contact.views import view2
from apps.contact.apps import ContactConfig

app_name = ContactConfig.name

urlpatterns = [
    path('', view2, name = "index"),
]