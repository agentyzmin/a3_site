# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 13:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_project'),
        ('projects', '0005_auto_20170215_1248'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='projectpost',
        #     name='blogpost_ptr',
        # ),
        # migrations.RemoveField(
        #     model_name='projectpost',
        #     name='related_project',
        # ),
        migrations.DeleteModel(
            name='ProjectPost',
        ),
    ]