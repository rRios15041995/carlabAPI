# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-18 04:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carlab_api', '0016_auto_20180117_2158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'subcategories'},
        ),
    ]