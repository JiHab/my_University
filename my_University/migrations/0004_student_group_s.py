# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-05 16:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_University', '0003_remove_student_group_s'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group_s',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_University.Group'),
        ),
    ]
