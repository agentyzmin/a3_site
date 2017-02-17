# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150527_1555'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='blogpost_ptr',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='related_project',
        ),
        migrations.AddField(
            model_name='project',
            name='content',
            field=mezzanine.core.fields.RichTextField(default='', verbose_name='Content'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='main_image',
            field=models.ImageField(upload_to='', verbose_name='main_image'),
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
