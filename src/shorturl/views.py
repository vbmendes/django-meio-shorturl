# -*- coding: utf8 -*-

"""
Created on 23/08/2010

@author vbmendes
"""

from django.http import HttpResponsePermanentRedirect, Http404

from core import real_url
from exceptions import InvalidShortId


def redirect(self, shortid):
    try:
        return HttpResponsePermanentRedirect(real_url(shortid))
    except InvalidShortId, e:
        raise Http404, str(e)
