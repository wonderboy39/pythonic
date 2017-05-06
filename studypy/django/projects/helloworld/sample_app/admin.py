# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from sample_app.models import VideoCategory, VideoUrl

# Register your models here.
admin.site.register(VideoUrl)
admin.site.register(VideoCategory)
