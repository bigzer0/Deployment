# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-04 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20170729_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='i_baseDir',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
