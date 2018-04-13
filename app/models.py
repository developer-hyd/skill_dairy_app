# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models




class Post(models.Model):
    subject = models.CharField(max_length=100, unique=True)
    topic = models.CharField(max_length=1000, null=True)
    description = models.TextField()
    # publication_date = models.DateField(default=Date)
    link1 = models.CharField(max_length=250)
    link2 = models.CharField(max_length=250)
    link3 = models.CharField(max_length=250)
    file = models.FileField()
    visibility = models.BooleanField(default=True)
