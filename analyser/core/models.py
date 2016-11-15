# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Document(models.Model):
    name = models.CharField('Nome', max_length=100)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.name