from django.contrib.sites.models import Site
from django.test import TestCase

from shorturl import conf
from shorturl.core import real_url, shorten

from models import URL


class ShortenModelTest(TestCase):
    fixtures = ['shorturl-test-data.json']

    def setUp(self):
        self.old_models = conf.MODELS
        conf.MODELS = {
            '': 'shorturl.URL',
        }
        conf.set_prefixes(conf.MODELS)

    def tearDown(self):
        if self.old_models is not None:
            conf.MODELS = self.old_models
            conf.set_prefixes(self.old_models)

    def test_shorten_123(self):
        self.assertEqual(
            shorten(URL.objects.get(pk=123)),
            'http://example.com/1z'
        )

    def test_shorten_321(self):
        self.assertEqual(
            shorten(URL.objects.get(pk=321)),
            'http://example.com/5B'
        )

    def test_real_url_1z(self):
        self.assertEqual(
            real_url('1z'),
            'http://google.com/',
        )

    def test_real_url_5B(self):
        self.assertEqual(
            real_url('5B'),
            'http://test.com/',
        )

