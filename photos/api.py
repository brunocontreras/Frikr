# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from photos.models import Photo
from photos.permissions import UserPermission
from photos.serializers import UserSerializer, PhotoSerializer, PhotoListSerializer
from photos.views_querysets import PhotoQuerySet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class UserViewSet(viewsets.ViewSet):

    permission_classes = (UserPermission,)

    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    # En el post creamos un nuevo usuario.
    # Da igual el id que enviemos, porque es de sólo lectura y generaría uno nuevo.
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # Detalle
    def retrieve(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Generalización para devolver el serializador de lista ó de clase según la acción
class ListDetailSerializer(object):
    list_serializer_class = None

    def get_serializer_class(self):
        return self.list_serializer_class if self.action.lower() == 'list' else self.serializer_class


class PhotoViewSet(PhotoQuerySet, ListDetailSerializer, viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PhotoSerializer
    list_serializer_class = PhotoListSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'description', 'owner__first_name', 'owner__last_name')
    ordering_fields = ('name', 'owner', 'created_on')

    def perform_create(self, serializer):
        """
        Al guardar, forzamos a que el owner sea el usuario autenticado
        """
        serializer.save(owner=self.request.user)