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
    return render(request, 'sample_app/show_vlist.html',{'test':'test'})
    #return HttpResponseRedirect(reverse('sample_app:show_vlist'))
    #return redirect('sample_app/show_vlist/')
    #return HttpResponseRedirect('sample_app:show_vlist')

#def list(request):
def show_vlist(request):
    print("view.py - list()")
    video_list = VideoUrl.objects.all().order_by('videourl_id')
    msg = { 'video_list' : video_list }
    #아래의 부분은 응? 어뜨케 고치지? ㅋㅋㅋ
    return render ( request, 'sample_app/show_vlist.html', msg )

