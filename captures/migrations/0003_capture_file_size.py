# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('captures', '0002_auto_20150803_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='capture',
            name='file_size',
            field=models.PositiveIntegerField(default='1'),
            preserve_default=False,
        ),
    ]
