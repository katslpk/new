import requests

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import ListView, FormView, CreateView

from apps.about.form import NewCarAddForm
from apps.about.models import CarInfo
from apps.onboarding.models import Profile


class CarInfoView(LoginRequiredMixin, ListView):
    template_name = "about/index.html"
    model = CarInfo
    success_url = reverse_lazy("about:index")

    def get_context_data_name(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = Profile.objects.get(user_id=user.id)
        context["name"] = profile.name
        return context

    def get_queryset(self):
        user = self.request.user
        queryset = CarInfo.objects.filter(user_id=user.id)
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            ctx["form"] = NewCarAddForm()

        return ctx

