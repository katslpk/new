from django.forms import ModelForm
from django import forms

from apps.service.models import Station


class StationAddForm(ModelForm):
    class Meta:
        model = Station
        widgets = {"user": forms.HiddenInput}
        fields = "__all__"
