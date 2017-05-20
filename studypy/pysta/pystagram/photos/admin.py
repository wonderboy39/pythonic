# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# 추가한 모델인 Photo에 대한 내용 수정
from .models import Photo
# Register your models here.

# 추가한 모델인 Photo에 대한 내용 수정
admin.site.register(Photo)
