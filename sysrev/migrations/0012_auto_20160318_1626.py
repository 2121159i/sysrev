# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sysrev', '0011_auto_20160318_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date_started',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='pool_size',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
