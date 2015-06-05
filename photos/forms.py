# -*- coding: utf-8 -*-
from django import forms
from photos.models import Photo


class LoginForm(forms.Form):

    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput())


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ()