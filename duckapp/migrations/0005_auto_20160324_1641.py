# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duckapp', '0004_auto_20160323_1849'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterField(
            model_name='answer',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
