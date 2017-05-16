# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from sample_app.models import VideoUrl, VideoCategory

# Create your views here.
def index(request):
    context = {'videourls' : 'helloworld'}
    return render(request, 'sample_app/index.html', context)

def write(request):
    return render(request, 'sample_app/write.html',{'test':'test'} )

def write_ok(request):
    print("category :: " + request.POST['category'])
    print("subject :: " + request.POST['subject'])
    print("url :: " + request.POST['url'])
    print("description :: " + request.POST['description'])
    m_subject = request.POST['subject']
    m_url = request.POST['url']
    m_description = request.POST['description']

    v = VideoUrl( subject=m_subject, url=m_url, description=m_description )
    #v.save(force_insert=True)
    v.save()
    #return render(request, 'sample_app/show_vlist.html',{'test':'test'})
    return HttpResponseRedirect(reverse('sample_app:show_vlist'),{'test':'test'})
    #return redirect('sample_app/show_vlist/')
    #return HttpResponseRedirect('sample_app:show_vlist')

#def list(request):
def show_vlist(request):
    print("view.py - list()")
    video_list = VideoUrl.objects.all()
    #vidoe_list = get_object_or_404(VideoUrl, pk=videourl_id)
    for vod in video_list:
        print('vod : ' + vod.subject)

    msg = { 'video_list' : video_list }
    #아래의 부분은 응? 어뜨케 고치지? ㅋㅋㅋ
    return render ( request, 'sample_app/show_vlist.html', msg )

def modify(request):
    msg = { 'temp' : 'temp'}
    return render( request, 'sample_app/modify.html', msg )