# -*- coding: utf-8 -*-
from django.conf.urls import url
from sample_app import views
from sample_app.views import VideoUrlUpdateView, VideoUpdateView
#app_name = 'sample_app'
urlpatterns = [
    #url(r'^sample_app/', include('smaple_app.urls', namespace="sample_app")),
    #url(r'^P<videourl_id>\d+/$', views.)
    url(r'^index/$', views.index, name='index'),
    url(r'^write/$', views.write, name='write'),
    url(r'^write_ok/$', views.write_ok, name='write_ok'),
    url(r'^show_vlist/$', views.show_vlist, name='show_vlist'),
    url(r'^modify/$', views.modify, name='modify'),
    url(r'^modify_ok/$', views.modify_ok, name='modify_ok'),
    # UpdateView 클래스 사용
    url(r'^(?P<pk>[0-9]+)/update/$', VideoUrlUpdateView.as_view(), name='update'),
    # View 클래스 이용
    url(r'^(?P<pk>[0-9]+)/mupdate/$', VideoUpdateView.as_view(), name='mupdate'),
]
