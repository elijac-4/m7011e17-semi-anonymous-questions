# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0006_auto_20171203_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]