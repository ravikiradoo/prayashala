# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-21 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrayaShala', '0016_tests_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='tests',
            name='Active',
            field=models.BooleanField(default=False),
        ),
    ]