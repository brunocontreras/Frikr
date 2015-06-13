# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from files.api import FilesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('files', FilesViewSet)

urlpatterns = patterns('',
    url(r'', include(router.urls))
)