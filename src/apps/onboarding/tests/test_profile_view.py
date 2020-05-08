from django.test import TestCase

from apps.onboarding.views.main import ProfileView
from project.utils.xtests import TemplateResponseTestMixin


class Test(TestCase, TemplateResponseTestMixin):
    def test_get(self):
        self.validate_response(
            url="/o/main/",
            expected_view_name="onboarding:main",
            expected_view=ProfileView,
            expected_template="onboarding/main.html",
        )
