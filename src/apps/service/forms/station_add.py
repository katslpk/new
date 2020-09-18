from django.forms import ModelForm

from apps.service.models import Station


class StationAddForm(ModelForm):
    class Meta:
        model = Station
        fields = "__all__"
