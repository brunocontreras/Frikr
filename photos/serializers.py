# -*- coding: utf-8 -*-
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from photos.models import Photo
from rest_framework import serializers

class UserSerializer(serializers.Serializer):

    # Estos son los campos que se van a mostrar en la respuesta.
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Crea una instancia de User a partir de los datos
        del diccionario validated_data.
        """

        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza una instancia de User a partir de los datos
        del diccionario validated_data.
        """
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')

        # la contraseña siempre hay que encriptarla
        instance.password = make_password(validated_data.get('password'))

        # En los formularios de Django guarda automáticamente.
        # Aquí no. Hay que hacerlo nosotros.
        instance.save()

        return instance



class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo

class PhotoListSerializer(PhotoSerializer):
    class Meta(PhotoSerializer.Meta):
        fields = ('id', 'name', 'url')