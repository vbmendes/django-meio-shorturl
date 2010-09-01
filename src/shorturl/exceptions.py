# -*- coding: utf8 -*-

"""
Created on 23/08/2010

@author vbmendes
"""


class ShortURLException(Exception):
    pass


class InvalidShortId(ValueError, ShortURLException):
    pass


class NoShortIdForObject(TypeError, ShortURLException):
    pass

