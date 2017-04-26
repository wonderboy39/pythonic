# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# 추가로직 - jayden
from django.http import HttpResponse
from .models import Photo
from django.shortcuts import get_object_or_404
# from photos.forms import create
from .forms import PhotoForm
from django.shortcuts import redirect

# Create your views here.
# 추가로직 - jayden
def hello(request):
    return HttpResponse('안녕하쉽늬까')

def detail(request,pk):
#    msg = '{}번 사진 보여주겠슴다'.format(pk)
#    photo = Photo.objects.get(pk=pk)
    photo = get_object_or_404(Photo, pk=pk)
    messages = ( 
        '<p>{pk}번 사진 출력합니다.</p>'.format(pk=photo.pk),
        '<p>주소는 {url}</p>'.format(url=photo.image.url),
        '<p><img src="{url}"/></p>'.format(url=photo.image.url),
    )
#    return HttpResponse('detail 뷰 함수')
#    return HttpResponse(msg)
    return HttpResponse('\n'.join(messages))

def create(request):
    form = PhotoForm()
    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return redirect(obj)
    ctx = {
        'form': form,
    }
    return render(request, 'edit.html', ctx)