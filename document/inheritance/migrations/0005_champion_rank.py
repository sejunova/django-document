# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inheritance', '0004_champion'),
    ]

    operations = [
        migrations.AddField(
            model_name='champion',
            name='rank',
            field=models.PositiveIntegerField(default=0),
        ),
    ]