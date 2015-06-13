# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from photos import api
from photos.api import PhotoViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

"""
    El api/1.0 lo quitamos de las urls porque lo vamos a poner desde el proyecto.
"""

photo_router = DefaultRouter()
photo_router.register(r'photos', PhotoViewSet)
# base_name lo necesita para crear los 'name' de las urls, lo que antes poníamos en cada url.
# No es capaz de resolverlo automáticamente porque no es ModelViewSet.
photo_router.register(r'users', UserViewSet, base_name='user')

urlpatterns = patterns('',
    url(r'', include(photo_router.urls)),
)
