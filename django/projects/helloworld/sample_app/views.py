# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from sample_app.models import VideoUrl, VideoCategory
from .VideoForm import VideoForm
from django.shortcuts import render, redirect

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
    video_list = VideoUrl.objects.all()
    #vidoe_list = get_object_or_404(VideoUrl, pk=videourl_id)
    for vod in video_list:
        print('vod : ' + vod.subject)
    msg = { 'video_list' : video_list }
    return render ( request, 'sample_app/show_vlist.html', msg )

def modify(request):
    if request.method == 'GET':
        vod = VideoUrl.objects.get(vod_id=request.GET['vod_id'])
        return render(request, 'sample_app/modify.html', {'vod':vod})
    elif request.method == 'POST':
        # 1) Form 클래스로 구현
        # modify 페이지 자체를 Form클래스로 구현할때의 페이지 구성
        form = VideoForm()
        ctx = {
            'form': form
        }
        return render(request, 'sample_app/modify.html',ctx)


def modify_ok(request):
    if request.method=='POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'sample_app/show_vlist.html', {'form' : form })
    return render(request, 'sample_app/show_vlist.html')