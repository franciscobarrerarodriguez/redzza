# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-13 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0005_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='main',
            field=models.BooleanField(default=False),
        ),
    ]