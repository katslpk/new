from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm

from apps.about.models import CarInfo

User = get_user_model()


class NewCarAddForm(ModelForm):
    class Meta:
        model = CarInfo
        widgets = {"user": forms.HiddenInput}
        fields = "__all__"


