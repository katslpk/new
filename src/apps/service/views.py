from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView

from apps.about.models import CarInfo
from apps.service.forms.add_work import AddWorkForm
from apps.service.models import Work


class CarWorkView(LoginRequiredMixin, ListView):
    template_name = "service/index.html"
    madel = CarInfo

    def get_queryset(self):
        user = self.request.user
        queryset = CarInfo.objects.filter(user_id=user.id)
        return queryset


class WorkView(LoginRequiredMixin, ListView):
    template_name = "service/work.html"
    model = Work


class AddWorkView(LoginRequiredMixin, CreateView):
    template_name = "service/add_work.html"
    form_class = AddWorkForm
    model = Work

    def get_success_url(self):
        url = reverse_lazy("service:index")
        return url
