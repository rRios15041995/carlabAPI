# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 20:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carlab_api', '0012_order_schedule_userbilling_userplate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='service',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserBilling',
        ),
        migrations.DeleteModel(
            name='UserPlate',
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
