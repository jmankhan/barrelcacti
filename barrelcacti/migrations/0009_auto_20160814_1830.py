# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-14 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barrelcacti', '0008_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(max_length=300),
        ),
    ]