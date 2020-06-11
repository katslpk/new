from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic import TemplateView

from apps.about.models import CarInfo
from apps.onboarding.models import Profile


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "about/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        user = self.request.user
        profile = Profile.objects.get(user_id=user.id)
        context["name"] = profile.name
        return context


class CarInfoView(LoginRequiredMixin, ListView):
    template_name = "about/index.html"
    model = CarInfo
