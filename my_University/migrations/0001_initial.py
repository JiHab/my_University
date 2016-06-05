# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-05 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('group_s', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_University.Group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='monitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_University.Student'),
        ),
    ]