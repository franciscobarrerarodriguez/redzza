# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-09 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_category_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(default='#FFFFFF', max_length=7),
        ),
    ]