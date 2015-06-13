# -*- coding: utf-8 -*-
from django.db.models import Q
from frikr.settings import PUBLIC
from photos.models import Photo


class PhotoQuerySet(object):

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
