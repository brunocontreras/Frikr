# -*- coding: utf-8 -*-
from files.models import File
from rest_framework.serializers import ModelSerializer


class FileSerializer(ModelSerializer):

    class Meta:
        model = File
        read_only_fields = ('owner',)
