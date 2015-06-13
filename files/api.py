# -*- coding: utf-8 -*-
from files.models import File
from files.serializers import FileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from celery_tasks import download_big_file

class FilesViewSet(GenericViewSet,
                   CreateModelMixin,
                   ListModelMixin,
                   RetrieveModelMixin,
                   DestroyModelMixin):

    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        download_big_file.delay()
        serializer.save(owner = self.request.user)