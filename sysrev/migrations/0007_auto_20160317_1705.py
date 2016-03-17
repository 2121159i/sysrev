# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sysrev', '0006_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='eyw_transactionref',
        ),
        migrations.AlterField(
            model_name='paper',
            name='review',
            field=models.ForeignKey(default=None, to='sysrev.Review'),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(to='sysrev.Researcher'),
        ),
    ]
