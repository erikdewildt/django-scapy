# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import captures.models


class Migration(migrations.Migration):

    dependencies = [
        ('captures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='capture',
            name='filename',
            field=models.CharField(default='new', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='capture',
            name='file',
            field=models.FileField(upload_to=captures.models.get_capture_file_path),
        ),
    ]
