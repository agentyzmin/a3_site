# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='project',
            field=models.ForeignKey(
                # default=django.db.models.deletion.SET_NULL,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='projects.Project'),
        ),
    ]
