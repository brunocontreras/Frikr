# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='owner',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='visibility',
            field=models.CharField(default=b'PUB', max_length=3, choices=[(b'PUB', b'P\xc3\xbablica'), (b'PRI', b'Privada')]),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='license',
            field=models.CharField(default=b'CC', max_length=3, choices=[(b'RIG', b'Copyright'), (b'LEF', b'Copyleft'), (b'CC', b'Creative Commons')]),
        ),
    ]
