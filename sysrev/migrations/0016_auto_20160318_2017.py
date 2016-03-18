# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sysrev', '0015_review_date_started'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='abstract_rev',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='paper',
            name='document_rev',
            field=models.NullBooleanField(default=None),
        ),
    ]
