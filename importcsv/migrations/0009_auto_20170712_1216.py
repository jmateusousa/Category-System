# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importcsv', '0008_auto_20170712_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Name Channel:'),
        ),
    ]
