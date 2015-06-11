# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import View
from photos.serializers import UserSerializer
from rest_framework.renderers import JSONRenderer


class UserListAPI(View):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        renderer = JSONRenderer()
        data = renderer.render(serializer.data)
        return HttpResponse(data)