# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from photos import views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^new', views.CreatePhotoView.as_view(), name='create_photo'),
    url(r'^profile', views.ProfileView.as_view(), name='profile'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^logout$', views.LogoutView.as_view(), name='logout'),
    url(r'^photos/?$', views.PhotoList.as_view(), name='photo_list'),
    url(r'^photos/(?P<pk>[0-9]+)$', views.PhotoDefailView.as_view(), name='photo_detail'),
)
