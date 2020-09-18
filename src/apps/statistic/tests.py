from unittest import skip

from django.test import TestCase

from apps.statistic.views import IndexView
from project.utils.xtests import TemplateResponseTestMixin


@skip
class Test(TestCase, TemplateResponseTestMixin):
    def test_get(self):
        self.validate_response(
            url="/statistic/",
            expected_view_name="statistic:index",
            expected_view=IndexView,
            expected_template="statistic/index.html",
        )
