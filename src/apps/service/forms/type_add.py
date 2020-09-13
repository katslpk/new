from django.forms import ModelForm

from apps.service.models import Type


class TypeAddForm(ModelForm):
    class Meta:
        model = Type
        fields = "__all__"
