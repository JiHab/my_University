# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-05 16:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_University', '0002_auto_20160605_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='group_s',
        ),
    ]
