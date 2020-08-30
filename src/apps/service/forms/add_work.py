from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm

from apps.service.models import Work

User = get_user_model()


class AddWorkForm(ModelForm):
    class Meta:
        model = Work
        widgets = {"user": forms.HiddenInput}
        fields = "__all__"
