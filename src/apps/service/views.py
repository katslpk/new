from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.service.forms.add_work import AddWorkForm
from apps.service.models import Work


class WorkView(LoginRequiredMixin, ListView):
    template_name = "service/index.html"
    model = Work

class AddWorkView(LoginRequiredMixin, CreateView):
    template_name = "service/add_work.html"
    form_class = AddWorkForm

    def get_success_url(self):
        url = reverse_lazy("service:index")
        return url