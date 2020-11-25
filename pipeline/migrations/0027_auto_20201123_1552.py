# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-23 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pipeline", "0026_auto_20201028_1049"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pipelineinstance",
            name="instance_id",
            field=models.CharField(db_index=True, max_length=32, unique=True, verbose_name="实例ID"),
        ),
    ]
