# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-16 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carlab_api', '0006_worker_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cat_name', models.CharField(max_length=100)),
                ('worker', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
            ],
        ),
    ]
