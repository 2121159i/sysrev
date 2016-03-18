# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sysrev', '0012_auto_20160318_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='abstract_rev',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='paper',
            name='document_rev',
            field=models.BooleanField(default=None),
        ),
    ]
