from django.views.generic import ListView

from apps.education.models import Education


class IndexView(ListView):
    template_name = "education/index.html"
    model = Education

