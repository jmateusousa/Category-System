# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importcsv', '0002_auto_20170710_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='category_sub',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='category_channel',
        ),
        migrations.AddField(
            model_name='channel',
            name='category_channel',
            field=models.ManyToManyField(to='importcsv.Category'),
        ),
    ]