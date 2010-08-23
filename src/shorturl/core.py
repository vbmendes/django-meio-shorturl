# -*- coding: utf8 -*-

"""
Created on 23/08/2010

@author: vbmendes
"""

from django.contrib.sites.models import Site

from baseconv import b62
import conf

def _get_prefix(obj):
    model = obj.__class__
    model_name = model._meta.app_label + '.' + model.__name__
    return conf.PREFIXES[model_name]

def _get_model(prefix = None):
    return conf.MODELS[prefix]

def shorten(obj):
    prefix = _get_prefix(obj)
    return 'http://' + Site.objects.get_current().domain + \
        '/' + prefix + b62.from_decimal(obj.pk)

