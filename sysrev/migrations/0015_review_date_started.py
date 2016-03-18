# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sysrev', '0014_remove_review_date_started'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date_started',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
