from django import forms
from django.forms import ModelForm

from apps.service.models import Station


class StationAddForm(ModelForm):
    class Meta:
        model = Station
        widgets = {"user": forms.HiddenInput}
        fields = "__all__"
