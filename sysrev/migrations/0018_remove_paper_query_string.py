# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sysrev', '0017_auto_20160319_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='query_string',
        ),
    ]
