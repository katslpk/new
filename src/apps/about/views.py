from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.views.generic import ListView

from apps.about.form import NewCarAddForm
from apps.about.models import CarInfo

User = get_user_model()


class ALLCarInfoView(LoginRequiredMixin, ListView):
    template_name = "about/index.html"
    model = CarInfo

    def get_queryset(self):
        user = self.request.user
        queryset = CarInfo.objects.filter(user_id=user.id)
        return queryset


class CarInfoView(LoginRequiredMixin, DetailView):
    template_name = "about/index_car.html"
    model = CarInfo


class CarAdd(LoginRequiredMixin, CreateView):
    form_class = NewCarAddForm
    template_name = "about/car_add.html"
    model = CarInfo

    def get_success_url(self):
        url = reverse_lazy("about:index")
        return url

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            ctx["form"] = NewCarAddForm(initial={"user": self.request.user})

        return ctx


class CarInfoDelete(DeleteView):
    model = CarInfo
    template_name = "about/index_delete.html"

    def get_success_url(self):
        url = reverse_lazy("about:index")
        return url
