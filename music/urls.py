# -*- coding: utf-8 -*-
# @Author: ShawnFiend
# @Date:   2016-06-18 17:58:23
# @Last Modified by:   root
# @Last Modified time: 2016-06-19 17:18:38

from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/<album_id>/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]

