from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from apps.education.models import Work


class IndexView(LoginRequiredMixin, ListView):
    template_name = "education/index.html"
    model = Work

