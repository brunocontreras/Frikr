# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from photos import api
from photos.api import PhotoViewSet
from rest_framework.routers import DefaultRouter

"""
    El api/1.0 lo quitamos de las urls porque lo vamos a poner desde el proyecto.
"""

photo_router = DefaultRouter()
photo_router.register(r'photos', PhotoViewSet)

urlpatterns = patterns('',
    url(r'^users/$', api.UserListAPI.as_view(), name='user_list_api'),
    url(r'^users/(?P<pk>[0-9]+)$', api.UserDetailAPI.as_view(), name='user_detail_api'),

    url(r'', include(photo_router.urls)),
)
