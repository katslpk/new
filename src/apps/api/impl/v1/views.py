from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.api.impl.v1.serializers import WorkSerializer
from apps.education.models import Work


class WorkViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = WorkSerializer

    def get_queryset(self):
        return Work.objects.all()
