from django.forms import ModelForm

from apps.service.models import Work


class AddWorkForm(ModelForm):
    class Meta:
        model = Work
        fields = '__all__'