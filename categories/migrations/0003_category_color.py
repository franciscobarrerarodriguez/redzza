# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-09 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='color',
            field=models.CharField(default='color', max_length=7),
            preserve_default=False,
        ),
    ]