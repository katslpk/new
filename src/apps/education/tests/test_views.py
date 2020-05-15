from django.test import TestCase

from apps.education.views import IndexView
from project.utils.xtests import TemplateResponseTestMixin


class Test(TestCase, TemplateResponseTestMixin):
    def test_get(self):
        self.validate_response(
            url="/education/",
            expected_view=IndexView,
            expected_view_name="education:index",
            expected_template="education/index.html",
        )
