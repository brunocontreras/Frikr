# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from photos.models import Photo

# Create your views here.

def home(request):
    photos = Photo.objects.filter(visibility=Photo.PUBLIC).order_by('-created_on')
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