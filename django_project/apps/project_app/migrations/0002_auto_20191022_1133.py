# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-22 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birth_date',
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(default='', max_length=255),
        ),
    ]
