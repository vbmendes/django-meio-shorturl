from django.contrib.sites.models import Site
from django.test import TestCase

from shorturl.core import shorten

from models import URL


class ShortenModelTest(TestCase):
    fixtures = ['shorturl-test-data.json']

    def test_shorten(self):
        self.assertEqual(
            shorten(URL.objects.get(pk=123)),
            'http://example.com/1z'
        )

