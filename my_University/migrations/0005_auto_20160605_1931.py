# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-05 16:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('my_University', '0004_student_group_s'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_birth',
            field=models.DateField(default=datetime.datetime(2016, 6, 5, 16, 31, 35, 580177, tzinfo=utc), verbose_name='Date 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='time_birth',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 5, 16, 31, 50, 423407, tzinfo=utc), verbose_name='Date 2'),
            preserve_default=False,
        ),
    ]
