# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-17 23:57
from __future__ import unicode_literals

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20170810_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatars/no-avatar.png', upload_to=profiles.models.File.generatePath),
        ),
    ]
