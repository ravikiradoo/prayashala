# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-06 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrayaShala', '0009_student_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='tests',
            name='No_of_Questions',
            field=models.IntegerField(default=0),
        ),
    ]
