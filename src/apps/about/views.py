from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView

from apps.about.form import NewCarAddForm
from apps.about.models import CarInfo
from apps.onboarding.models import Profile

User = get_user_model()


class CarInfoView(LoginRequiredMixin, ListView):
    template_name = "about/index.html"
    model = CarInfo

    def get_queryset(self):
        user = self.request.user
        queryset = CarInfo.objects.filter(user_id=user.id)
        return queryset


class CarAdd(LoginRequiredMixin, CreateView):
    form_class = NewCarAddForm
    template_name = "about/car_add.html"

    def get_success_url(self):
        url = reverse_lazy("about:index")
        return url

    # def form_valid(self, form):
    #     form.instance.user = User.objects.get(user=self.request.username)
    #     return super(CarAdd, self).form_valid(form)
