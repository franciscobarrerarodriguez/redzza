# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-06 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20170906_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]