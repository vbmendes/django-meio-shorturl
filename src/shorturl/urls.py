# -*- coding: utf8 -*-

"""
Created on 23/08/2010

@author vbmendes
"""

from django.conf.urls.defaults import *

import conf


urlpatterns = patterns('', 
    url(
        regex = '^(?P<shortid>\w+)$',
        view  = 'shorturl.views.redirect',
    ),
)

