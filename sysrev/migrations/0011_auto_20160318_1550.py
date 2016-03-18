# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sysrev', '0010_auto_20160317_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researcher',
            name='forename',
        ),
        migrations.RemoveField(
            model_name='researcher',
            name='surname',
        ),
    ]
