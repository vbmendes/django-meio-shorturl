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

