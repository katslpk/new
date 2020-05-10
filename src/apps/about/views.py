from django.views.generic import TemplateView

from apps.about.models import UserInfo


class IndexView(TemplateView):
    template_name = "about/index.html"
