# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pubmed_id', models.IntegerField()),
                ('title', models.CharField(default=b'', max_length=128)),
                ('authors', models.CharField(default=b'', max_length=128)),
                ('abstract', models.CharField(default=b'', max_length=4096)),
                ('paper_url', models.URLField(default=None, null=True, blank=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)),
                ('abstract_rev', models.NullBooleanField(default=None)),
                ('document_rev', models.NullBooleanField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('string', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128)),
                ('date_started', models.DateTimeField(default=django.utils.timezone.now)),
                ('query_string', models.CharField(max_length=128)),
                ('user', models.ForeignKey(to='sysrev.Researcher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='query',
            name='review',
            field=models.ForeignKey(to='sysrev.Review', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='paper',
            name='review',
            field=models.ForeignKey(default=None, to='sysrev.Review'),
            preserve_default=True,
        ),
    ]
