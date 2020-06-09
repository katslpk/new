import json

import requests
from django.http import HttpResponse
from django.views import View
from dynaconf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.api.impl.v1.serializers import WorkSerializer
from apps.education.models import Work


class WorkViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = WorkSerializer

    def get_queryset(self):
        return Work.objects.all()


class TelegramView(View):
    def post(self, *args, **kwargs):
        try:
            payload = json.loads(self.request.body)
            message = payload["message"]
            text = message["text"]
            chat_id = message["chat"]["id"]

            r = requests.post(
                f"https://api.telegram.org/bot{settings.TG}/sendMessage",
                json={"chat_id": chat_id, "text": text.upper()},
            )
            print(f"XXX sendMessage resp: {r}")
        except Exception as err:
            print(err)
        return HttpResponse()
