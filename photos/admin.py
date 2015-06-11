# -*- coding: utf-8 -*-
from django.contrib import admin
from photos.models import Photo

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):

    list_display = ('name', 'owner_name', 'license', 'visibility')
    list_filter = ('license', 'visibility', 'created_on')
    search_fields = ('name', 'description')

    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name',)
        }),
        ('Description', {
            'classes': ('wide',),
            'fields': ('description',)
        }),
        ('Author', {
            'classes': ('wide',),
            'fields': ('owner',)
        }),
        ('URL', {
            'classes': ('wide',),
            'fields': ('url',)
        }),
        ('License & Visibility', {
            'classes': ('wide', 'collapse'),
            'fields': ('license', 'visibility',)
        })
    )


    # Se lanza por por cada línea que tiene que pintar, obteniendo el objeto (en este caso photo)
    def owner_name(self, obj):
        return obj.owner.first_name + ' ' + obj.owner.last_name
    owner_name.short_description = 'Author'
    owner_name.admin_order_field = 'owner__first_name' # El doble guión bajo es para hacer un join, para acceder a un campo de una tabla relacional


# Habilita la entidad photo en el administrador de Django
admin.site.register(Photo, PhotoAdmin)