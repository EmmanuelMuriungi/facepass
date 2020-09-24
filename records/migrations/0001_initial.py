# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-26 08:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('program', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),                
                ('occupation', models.CharField(max_length=150, null=True)),                
                ('recorded_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
