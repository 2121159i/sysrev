# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sysrev', '0020_auto_20160320_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='paper_url',
            field=models.URLField(default=None, null=True, blank=True),
        ),
    ]
