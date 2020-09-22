from django import forms
from django.forms import ModelForm

from apps.service.models import Type


class TypeAddForm(ModelForm):
    class Meta:
        model = Type
        widgets = {"user": forms.HiddenInput}
        fields = "__all__"
