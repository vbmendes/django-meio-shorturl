# -*- coding: utf8 -*-

from django.db import models

class URL(models.Model):
    url = models.URLField(max_length = 100)

    class Meta:
        app_label = 'shorturl'

    def __unicode__(self):
        return self.url

    def get_absolute_url(self):
        return self.url


class Person(models.Model):
    name = models.CharField(max_length = 100)

    class Meta:
        app_label = 'shorturl'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return u'/people/%d/' % (self.pk)

