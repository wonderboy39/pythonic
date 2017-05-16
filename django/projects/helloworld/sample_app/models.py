# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class VideoCategory(models.Model):
    category = models.CharField(max_length=20)
    #pub_date = models.DateTimeField('date published') # 추후 다시 추가
    def __unicode__(self):
        return self.category

class VideoUrl(models.Model):
    #category = models.ForeignKey(VideoCategory)
    vod_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    #pub_date = models.DateTimeField('date published') # 추후 다시 추가
    def __unicode__(self):
        return self.subject
