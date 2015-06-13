# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20150529_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, null=True, validators=[photos.validators.badwords]),
        ),
        migrations.AlterField(
            model_name='photo',
            name='license',
            field=models.CharField(default=b'CC', max_length=3, choices=[(b'GRO', b'Gromenauer'), (b'RIG', b'Copyright'), (b'LEF', b'Copyleft'), (b'CC', b'Creative Commons')]),
        ),
    ]
