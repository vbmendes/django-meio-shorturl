# -*- coding: utf8 -*-

"""
Created on 23/08/2010

@author vbmendes
"""

from django.test import TestCase

from shorturl import conf


class RedirectTest(TestCase):
    urls = 'shorturl.urls'
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

    def test_redirect_view_1z(self):
        response = self.client.get('/1z')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response['Location'], 'http://google.com/')

    def test_redirect_view_5B(self):
        response = self.client.get('/5B')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response['Location'], 'http://test.com/')

    def test_redirect_view_object_does_not_exists(self):
        response = self.client.get('/6B')
        self.assertEqual(response.status_code, 404)

class PrefixedRedirectTest(TestCase):
    urls = 'shorturl.urls'
    fixtures = ['shorturl-test-data.json']

    def setUp(self):
        self.old_models = conf.MODELS
        conf.MODELS = {
            'u': 'shorturl.URL',
        }
        conf.set_prefixes(conf.MODELS)

    def tearDown(self):
        if self.old_models is not None:
            conf.MODELS = self.old_models
            conf.set_prefixes(self.old_models)

    def test_redirect_view_1z(self):
        response = self.client.get('/u1z')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response['Location'], 'http://google.com/')

    def test_redirect_view_5B(self):
        response = self.client.get('/u5B')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response['Location'], 'http://test.com/')

    def test_redirect_view_incorrect_prefix(self):
        response = self.client.get('/a1z')
        self.assertEqual(response.status_code, 404)

