# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-10 02:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20170810_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='icono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Icon'),
        ),
    ]
