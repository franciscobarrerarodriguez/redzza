# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-05 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0021_auto_20170405_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[(b'F', b'Femenino'), (b'M', b'Masculino')], default=b'M', max_length=1),
        ),
    ]
