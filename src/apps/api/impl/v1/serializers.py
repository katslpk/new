from rest_framework import serializers

from apps.service.models import Work


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"
