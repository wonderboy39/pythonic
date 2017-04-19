# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# django의 db패키지 내에 있는 models 모듈을 import
from django.db import models

# Create your models here.
class Photo(models.Model):
    image = models.ImageField()
    filtered_image = models.ImageField()
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
