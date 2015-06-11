# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from photos.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class UserListAPI(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)