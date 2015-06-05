"""frikr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from photos import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^new', views.CreatePhotoView.as_view(), name='create_photo'),
    url(r'^profile', views.ProfileView.as_view(), name='profile'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^logout$', views.LogoutView.as_view(), name='logout'),
    url(r'^photos/(?P<pk>[0-9]+)$', views.PhotoDefailView.as_view(), name='photo_detail'),
]
