from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import models
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView

from apps.about.models import CarInfo
from apps.service.models import Work


class ALLCarView(LoginRequiredMixin, ListView):
    template_name = "service/index.html"
    model = Work

    def get_queryset(self):
        own_cars = CarInfo.objects.filter(user_id=self.request.user)
        return own_cars


class CarWorkView(LoginRequiredMixin, ListView):
    template_name = "service/work.html"
    model = Work

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["work"] = Work.objects.all
        return context

    def get_queryset(self, **kwargs):
        return Work.objects.filter(car_model_id=self.kwargs["pk"])


class AddWorkView(LoginRequiredMixin, CreateView):
    template_name = "service/add_work.html"
    model = Work

    def get_form_class(self) -> type:
        own_cars = CarInfo.objects.filter(user_id=self.request.user)

        class TaskForm(forms.ModelForm):
            car_model = models.ModelChoiceField(queryset=own_cars)

            class Meta:
                model = Work
                fields = "__all__"

        return TaskForm

    def get_success_url(self):
        url = reverse_lazy("service:work")
        return url
