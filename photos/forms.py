# -*- coding: utf-8 -*-
from django import forms
from photos.models import Photo
from django.conf import settings


class LoginForm(forms.Form):

    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput())


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('owner',)

    # Limpia el formulario, no sólo valida sino que normaliza los valores recibidos.
    # se llama al clean del padre porque ya hace una limpieza.
    def clean(self):
        cleaned_data = super(PhotoForm, self).clean()
        description = cleaned_data.get('description', '')
        for badword in BADWORDS:
            if badword.lower() in description.lower():
                raise forms.ValidationError(badword + u" no está admitida")
        return cleaned_data