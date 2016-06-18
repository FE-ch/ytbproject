# -*- coding: utf-8 -*-
# @Author: ShawnFiend
# @Date:   2016-06-18 17:58:23
# @Last Modified by:   ShawnFiend
# @Last Modified time: 2016-06-19 01:12:03

from django.conf.urls import url
from . import views

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/31
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /m
]

