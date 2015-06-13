# -*- coding: utf-8 -*-
import urllib
from celery.task import task

# Hay que ejecutar el broker, el RabbitMQ. Descargar el programa y ejecutarlo desde la consola.

# Después de poner el celery hay que hacer un makemigrations y migrate

# para cargar celery hay que poner dentro del entorno:
# python manage.py celery worker
@task
def download_big_file():
    print "Downloading..."
    url = "http://politic365.com/wp-content/blogs.dir/1/files/2012/12/Calvin-Candie-Django-1.jpg"
    urllib.urlretrieve(url, "django.jpg")
    print "Finish"
    return "Tomaa"
