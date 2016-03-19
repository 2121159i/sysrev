# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sysrev', '0016_auto_20160318_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='pool_size',
        ),
        migrations.AlterField(
            model_name='paper',
            name='authors',
            field=models.CharField(default=b'', max_length=128),
        ),
    ]
