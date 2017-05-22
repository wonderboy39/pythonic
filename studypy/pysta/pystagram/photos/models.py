# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# django의 db패키지 내에 있는 models 모듈을 import
from django.db import models
from django.core.urlresolvers import reverse_lazy

# Create your models here.
class Photo(models.Model):
#    image = models.ImageField(upload_to='uploads/%Y/%m/%d/orig')
#    filtered_image = models.ImageField(upload_to='uploads/%Y/%m/%d/filtered')
    image = models.ImageField(upload_to='%Y/%m/%d/orig')
    filtered_image = models.ImageField(upload_to='%Y/%m/%d/filtered')
    content = models.TextField(max_length=300,blank=True,null=True)
    #created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField()

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.filtered_image.delete()
        super(Photo, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        url = reverse_lazy('detail', kwargs={'pk': self.pk})
        return url