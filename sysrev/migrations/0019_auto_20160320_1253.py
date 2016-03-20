# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sysrev', '0018_remove_paper_query_string'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.CharField(max_length=4096),
        ),
    ]
