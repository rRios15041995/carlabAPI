# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-08 00:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carlab_api', '0002_auto_20180108_0037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]