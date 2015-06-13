from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

UPLOAD_FOLDER = getattr(settings, 'UPLOAD_FOLDER', 'uploads')

class File(models.Model):

    file = models.FileField(upload_to=UPLOAD_FOLDER)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User)