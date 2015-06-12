# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from photos import api

"""
    El api/1.0 lo quitamos de las urls porque lo vamos a poner desde el proyecto.
"""

urlpatterns = patterns('',
    url(r'^/users/$', api.UserListAPI.as_view(), name='user_list_api'),
    url(r'^/users/(?P<pk>[0-9]+)$', api.UserDetailAPI.as_view(), name='user_detail_api'),
)
