# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from sample_app.models import VideoUrl, VideoCategory

# Create your views here.
def index(request):
    context = {'videourls' : 'helloworld'}
    return render(request, 'sample_app/index.html', context)

def write(request):
    return render(request, 'sample_app/write.html',{'test':'test'} )

def write_ok(request):
    print("subject :: " + request.POST['subject'])
    print("url :: " + request.POST['url'])
    return render(request, 'sample_app/write_ok.html',{'test':'test'})
