# -*- coding: utf8 -*-

"""
Created on 23/08/2010

@author: vbmendes
"""

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

MODELS = getattr(settings, 'SHORTURL_MODELS', None)
if not MODELS:
    raise ImproperlyConfigured, "In order to use django-shorturl you" \
        "must provide SHORTURL_MODELS setting."

def set_prefixes(models):
    globals()['PREFIXES'] = dict([(v, k) for k, v in models.items()])

set_prefixes(MODELS)

def get_base_url():
    if hasattr(settings, 'SHORTURL_BASE_URL'):
        return settings.SHORTURL_BASE_URL
    if not globals().has_key('_BASE_URL'):
        from django.contrib.sites.models import Site
        globals()['_BASE_URL'] = 'http://' + Site.objects.get_current().domain
    return globals()['_BASE_URL']

