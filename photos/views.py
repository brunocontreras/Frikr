# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from frikr.settings import PUBLIC
from photos.forms import LoginForm
from photos.forms import PhotoForm
from photos.models import Photo
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.views.generic import ListView


class HomeView(View):
    def get(self, request):
        photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_on')
        context = {
            'photo_list': photos[:5],
        }
        return render(request, 'photos/home.html', context)

class PhotoDefailView(View):
    def get(self, request, pk):

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


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('/')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'photos/login.html', context)


    def post(self, request):
        form = LoginForm(request.POST)
        context = {
            'form': form
        }
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


class ProfileView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        context = {
            'photos': request.user.photo_set.all()
        }
        return render(request, 'photos/profile.html', context)


class CreatePhotoView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        message = ''
        form = PhotoForm()
        context = {
            'form': form,
            'message': message
        }
        return render(request, 'photos/new_photo.html', context)

    def post(self, request):
        message = ''
        photo_with_user = Photo(owner=request.user)
        #photo_with_user.owner = request.user

        form = PhotoForm(request.POST, instance=photo_with_user)
        if form.is_valid():
            new_photo = form.save()
            message = 'Guardado con éxito! <a href="{0}">Ver foto</a>'.format(reverse('photo_detail', args=[new_photo.pk]))
            form = PhotoForm()
        context = {
            'form': form,
            'message': message
        }
        return render(request, 'photos/new_photo.html', context)


class PhotoList(ListView):
    model = Photo
    template_name = 'photos/list_of_photos.html'

    def get_queryset(self):
        # si el usuario no está autenticado, sólo las públicas
        if not self.request.user.is_authenticated():
            return Photo.objects.filter(visibility=PUBLIC)

        # si es superadmin, todas
        elif self.request.user.is_superuser:
            return Photo.objects.all()

        # si el usuario está autenticado y no es super admin, las suyas o las públicas de otros
        # para hacer un OR se utilizan los objetos Q. Se concatenan y se le pasa a filter.
        else:
            return Photo.objects.filter(
                Q(owner=self.request.user) | Q(visibility=PUBLIC)
            )

        return super(PhotoList, self).get_queryset()