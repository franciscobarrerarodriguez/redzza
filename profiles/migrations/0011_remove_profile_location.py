# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 17:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20170328_0410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
