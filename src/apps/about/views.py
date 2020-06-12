from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from apps.about.models import CarInfo
from apps.onboarding.models import Profile


class CarInfoView(LoginRequiredMixin, ListView):
    template_name = "about/index.html"
    model = CarInfo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = Profile.objects.get(user_id=user.id)
        context["name"] = profile.name
        return context

    def get_queryset(self):
        user = self.request.user
        queryset = CarInfo.objects.filter(user_id=user.id)
        return queryset
