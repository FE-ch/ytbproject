# -*- coding: utf-8 -*-
# @Author: ShawnFiend
# @Date:   2016-06-18 17:58:23
# @Last Modified by:   root
# @Last Modified time: 2016-06-20 23:51:47

from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/<album_id>/favorite
    # url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]

