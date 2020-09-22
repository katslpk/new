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

    def clean_start_mileage(self):

        cleaned = self.cleaned_data["start_mileage"]

        if cleaned < 0:
            raise forms.ValidationError("Mileage cannot be negative")
        return cleaned
