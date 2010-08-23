# -*- coding: utf8 -*-

"""
Created on 23/08/2010

@author: vbmendes
"""

import urlparse

from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db.models import get_model

from baseconv import b62
import conf
from exceptions import InvalidShortId


def _get_prefix(obj):
    model = obj.__class__
    model_name = model._meta.app_label + '.' + model.__name__
    return conf.PREFIXES[model_name]


def _get_model(short):
    i = 0
    while i < len(short):
        try:
            return conf.MODELS[short[:i]], short[i:]
        except KeyError:
            i += 1
    raise InvalidShortId, "No prefix found for %s." % short


def real_url(short):
    model, b62pk = _get_model(short)
    model = get_model(*model.split("."))
    try:
        obj = model.objects.get(pk = b62.to_decimal(b62pk))
    except model.DoesNotExist, e:
        raise InvalidShortId, str(e)
    return urlparse.urljoin(conf.get_base_url(), obj.get_absolute_url())


def shorten(obj):
    prefix = _get_prefix(obj)
    shortid = prefix + b62.from_decimal(obj.pk)
    return urlparse.urljoin(
        conf.get_base_url(),
        reverse('shorturl__redirect', args=(shortid,))
    )

