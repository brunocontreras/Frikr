# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from frikr.settings import PUBLIC
from photos.forms import LoginForm
from photos.forms import PhotoForm
from photos.models import Photo
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse

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
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if request.method.lower() == 'post':
        if form.is_valid():
            user_username = form.cleaned_data.get('username', '')
            user_password = form.cleaned_data.get('password', '')
            user = authenticate(username=user_username, password=user_password)
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    url = request.GET.get('next', 'profile')
                    return redirect(url)
                else:
                    context['errors'] = 'El usuario no está activo'
            else:
                context['errors'] = 'Usuario o contraseña incorrectos'

    return render(request, 'photos/login.html', context)

@login_required(login_url='login')
def profile(request):
    context = {
        'photos': request.user.photo_set.all()
    }
    return render(request, 'photos/profile.html', context)


@login_required(login_url='login')
def create_photo(request):
    message = ''
    if request.method.lower() == 'post':
        photo_with_user = Photo(owner=request.user)
        #photo_with_user.owner = request.user

        form = PhotoForm(request.POST, instance=photo_with_user)
        if form.is_valid():
            new_photo = form.save()
            message = 'Guardado con éxito! <a href="{0}">Ver foto</a>'.format(reverse('photo_detail', args=[new_photo.pk]))
            form = PhotoForm()
    else:
        form = PhotoForm()
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'photos/new_photo.html', context)