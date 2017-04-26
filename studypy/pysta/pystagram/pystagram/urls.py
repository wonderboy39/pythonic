# -*- coding: utf-8 -*-
"""pystagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# Added, Jayden
from photos.views import hello 
from photos.views import detail

# Added2, Jayden
from django.conf import settings
from django.conf.urls.static import static
from photos.views import create

urlpatterns = [
    url(r'^hello/$', hello),
    url(r'^photos/(?P<pk>[0-9]+)/$', detail, name='detail'),
    url(r'^photos/upload/$', create, name='create'),
    url(r'^admin/', admin.site.urls),
]

#MEDIA_URL = '/upload_files/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

urlpatterns += static('upload_files', document_root=settings.MEDIA_ROOT)

