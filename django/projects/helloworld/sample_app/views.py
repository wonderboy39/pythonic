# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from sample_app.models import VideoUrl, VideoCategory
from .VideoForm import VideoForm
from django.shortcuts import render, redirect
from pprint import pprint

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
    #just value test.
    for vod in video_list:
        print('vod : ' + vod.subject)

    msg = { 'video_list' : video_list }
    return render ( request, 'sample_app/show_vlist.html', msg )

def modify(request):
    if request.method == 'GET':
        vod = VideoUrl.objects.get(vod_id=request.GET['vod_id'])
        return render(request, 'sample_app/modify.html', {'vod':vod})
    elif request.method == 'POST':
        # 참고 URL : https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/#the-save-method
        # 1) Form 클래스로 구현
        # modify 페이지 자체를 Form클래스로 구현할때의 페이지 구성, POST방식

        # vod_id에 대한 하나의 데이터(로우) 얻어오기
        vod = VideoUrl.objects.get(vod_id=request.POST['vod_id'])

        # 하나의 로우는 model instance라고 하는가보다. instance 값으로 model 데이터를 넘겨준다.
        form = VideoForm(instance=vod)
        ctx = {
            'form': form
        }

        # form데이터를 실어서 modify.html로 전송
        return render(request, 'sample_app/modify.html',ctx)

def modify_ok(request):
    if request.method=='POST':
        # 단순 저장이 아닌 update구문으로 변경할 것
        # 원인) 단순 저장할 경우 복사본 데이터가 생성된다.
        # 방법) Model instance를 얻어온 후 해당 값들을 업데이트 해주는 수밖에.
        form = VideoForm(request.POST)
        if form.is_valid():
            vod = VideoUrl.objects.get(pk=request.POST['vod_id'])
            # vod.objects.update(force_update=True)
            # VideoUrl.objects.update(force_update=True)
            return render(request, 'sample_app/show_vlist.html', {'form' : form })
    return render(request, 'sample_app/show_vlist.html')