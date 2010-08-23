# -*- coding: utf8 -*-

"""
Created on 23/08/2010

@author: vbmendes
"""

from django.contrib.sites.models import Site
from django.db.models import get_model

from baseconv import b62
import conf


def _get_prefix(obj):
    model = obj.__class__
    model_name = model._meta.app_label + '.' + model.__name__
    return conf.PREFIXES[model_name]


def _get_model(short):
    i = 0
    while True:
        try:
            return conf.MODELS[short[:i]], short[i:]
        except KeyError:
            i += 1


def real_url(short):
    model, b62pk = _get_model(short)
    model = get_model(*model.split("."))
    obj = model.objects.get(pk = b62.to_decimal(b62pk))
    return obj.get_absolute_url()


def shorten(obj):
    prefix = _get_prefix(obj)
    return 'http://' + Site.objects.get_current().domain + \
        '/' + prefix + b62.from_decimal(obj.pk)

