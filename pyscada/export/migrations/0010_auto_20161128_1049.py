# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 10:49
from __future__ import unicode_literals

from django.db import migrations, models
import pyscada.export.models


class Migration(migrations.Migration):

    dependencies = [
        ('export', '0009_auto_20161128_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exporttask',
            name='datetime_start',
            field=models.DateTimeField(default=pyscada.export.models.datetime_now),
        ),
    ]
