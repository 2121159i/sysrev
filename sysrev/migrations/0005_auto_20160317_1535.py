# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sysrev', '0004_paper_query_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to='sysrev.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='paper',
            old_name='description',
            new_name='abstract',
        ),
        migrations.RenameField(
            model_name='query',
            old_name='description',
            new_name='string',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='user',
        ),
        migrations.RemoveField(
            model_name='query',
            name='query_string',
        ),
        migrations.RemoveField(
            model_name='query',
            name='title',
        ),
        migrations.RemoveField(
            model_name='query',
            name='user',
        ),
        migrations.AddField(
            model_name='paper',
            name='abstract_rev',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='paper',
            name='authors',
            field=models.CharField(default=None, max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='paper',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='paper',
            name='document_rev',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='paper',
            name='paper_url',
            field=models.URLField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='paper',
            name='review',
            field=models.ForeignKey(to='sysrev.Review', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='query',
            name='review',
            field=models.ForeignKey(to='sysrev.Review', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='eyw_transactionref',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(to='sysrev.UserProfile'),
        ),
    ]
