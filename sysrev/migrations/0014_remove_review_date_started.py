# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sysrev', '0013_auto_20160318_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='date_started',
        ),
    ]
