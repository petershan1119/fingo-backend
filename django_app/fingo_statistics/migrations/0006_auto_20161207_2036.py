# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-07 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fingo_statistics', '0005_auto_20161207_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]