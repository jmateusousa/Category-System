# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 11:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('importcsv', '0006_auto_20170711_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='subunlimited',
        ),
    ]