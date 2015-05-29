from django.contrib import admin
from photos.models import Photo

# Register your models here.

# Habilita la entidad photo en el administrador de Django
admin.site.register(Photo)