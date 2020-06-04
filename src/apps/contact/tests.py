from unittest import skip

from django.test import TestCase

from apps.contact.views import IndexView
from project.utils.xtests import TemplateResponseTestMixin


@skip
class Test(TestCase, TemplateResponseTestMixin):
    def test_get(self):
        self.validate_response(
            url="/contact/",
            expected_view_name="contact:index",
            expected_view=IndexView,
            expected_template="contact/index.html",
        )
