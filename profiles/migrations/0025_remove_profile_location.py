# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-06 00:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0024_auto_20170405_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
