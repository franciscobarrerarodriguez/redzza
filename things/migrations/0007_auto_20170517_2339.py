# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-17 23:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0029_auto_20170517_2339'),
        ('things', '0006_auto_20170508_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentary', models.CharField(max_length=500)),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='things.Notice')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='things.Notice')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='uploads')),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='things.Notice')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='delivery',
            field=models.CharField(choices=[('E', 'Yo mismo lo entrego'), ('C', 'Convenio'), ('R', 'Redzza service')], default='Convenio', max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='state',
            field=models.CharField(choices=[('N', 'Nuevo'), ('U', 'Usado'), ('E', 'Por Encargo'), ('B', 'Restaurado'), ('N', 'Renovado')], default='Nuevo', max_length=1),
        ),
    ]
