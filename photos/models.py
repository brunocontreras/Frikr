# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Photo(models.Model):

    COPYRIGHT = 'RIG'
    COPYLEFT = 'LEF'
    CREATIVE_COMMONS = 'CC'

    LICENSES = (
        (COPYRIGHT, 'Copyright'),
        (COPYLEFT, 'Copyleft'),
        (CREATIVE_COMMONS, 'Creative Commons'),
    )

    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # Pone la fecha automáticamente cuando se crea
    modified_on = models.DateTimeField(auto_now=True) # Pone la fecha automáticamente cuando se guarda
    # choices es una tupla que desplegará luego en la web todas las opciones.
    # ponemos una tupla para que sea inmutable. Podríamos haber utilizado un diccionario.
    license = models.CharField(max_length=3, choices=LICENSES)

    # Función que muestra en el admin el nombre de la entidad
    def __unicode__(self):
        return self.name