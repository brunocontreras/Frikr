# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from photos.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class UserListAPI(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    # En el post creamos un nuevo usuario.
    # Da igual el id que enviemos, porque es de sólo lectura y generaría uno nuevo.
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)