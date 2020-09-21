from django.forms import ModelForm
from django.forms import forms

from apps.service.models import Work


class WorkAddForm(ModelForm):
    class Meta:
        model = Work
        fields = "__all__"

    def clean_mileage(self):

        cleaned = self.cleaned_data["mileage"]

        if cleaned < 0:
            raise forms.ValidationError("Mileage cannot be negative")
        return cleaned

    def clean_cost(self):

        cleaned = self.cleaned_data["cost"]

        if cleaned < 0:
            raise forms.ValidationError("cost cannot be negative")
        return cleaned
