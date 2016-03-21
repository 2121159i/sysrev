# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    replaces = [(b'sysrev', '0001_initial'), (b'sysrev', '0002_auto_20160309_1952'), (b'sysrev', '0003_userprofile'), (b'sysrev', '0004_paper_query_review'), (b'sysrev', '0005_auto_20160317_1559'), (b'sysrev', '0005_auto_20160317_1535'), (b'sysrev', '0006_merge')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='sysrev.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('abstract', models.CharField(max_length=128)),
                ('query_string', models.CharField(max_length=128)),
                ('abstract_rev', models.BooleanField(default=False)),
                ('authors', models.CharField(default=None, max_length=128)),
                ('date', models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)),
                ('document_rev', models.BooleanField(default=False)),
                ('paper_url', models.URLField(default=None)),
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
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128)),
                ('query_string', models.CharField(max_length=128)),
                ('user', models.ForeignKey(to='sysrev.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='paper',
            name='review',
            field=models.ForeignKey(default=None, to='sysrev.Review'),
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
            name='forename',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='surname',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
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
    ]
