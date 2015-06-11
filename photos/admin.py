from django.contrib import admin
from photos.models import Photo

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):

    list_display = ('name', 'owner', 'license', 'visibility')
    list_filter = ('license', 'visibility', 'created_on')
    search_fields = ('name', 'description')


# Habilita la entidad photo en el administrador de Django
admin.site.register(Photo, PhotoAdmin)