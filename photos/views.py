# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from frikr.settings import PUBLIC
from photos.models import Photo
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate

# Create your views here.

def home(request):
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_on')
    context = {
        'photo_list': photos[:5],
    }
    return render(request, 'photos/home.html', context)

def photo_detail(request, pk):

    '''
    Este es mucho más bonito.

    possible_photos = Photo.objects.filter(pk=pk)
    if len(possible_photos) <= 0:
        return HttpResponseNotFound('No existe la foto')
    else:
        photo = possible_photos[0]
        context = {
            'photo': photo
        }
        return render(request, 'photos/photo_detail.html', context)
    '''

    try:
        photo = Photo.objects.get(pk=pk)
        context = {
            'photo': photo
        }
        return render(request, 'photos/photo_detail.html', context)

    except Photo.DoesNotExist:
        return HttpResponseNotFound("No existe la foto")


def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('/')


def login(request):
    context = {}
    if request.method.lower() == 'post':
        user_username = request.POST.get('username', '')
        user_password = request.POST.get('password', '')
        user = authenticate(username=user_username, password=user_password)
        if user is not None:
            if user.is_active:
                django_login(request, user)
                return redirect('/')
            else:
                context['errors'] = 'El usuario no está activo'
        else:
            context['errors'] = 'Usuario o contraseña incorrectos'

    return render(request, 'photos/login.html', context)