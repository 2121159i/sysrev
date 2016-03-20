# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sysrev', '0019_auto_20160320_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='pubmed_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.CharField(default=b'', max_length=4096),
        ),
        migrations.AlterField(
            model_name='paper',
            name='title',
            field=models.CharField(default=b'', max_length=128),
        ),
    ]
