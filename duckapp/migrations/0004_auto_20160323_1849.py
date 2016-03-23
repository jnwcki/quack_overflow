# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 18:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('duckapp', '0003_answer_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 23, 18, 49, 8, 743446, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 23, 18, 49, 20, 466041, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sign_up_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 23, 18, 49, 39, 323700, tzinfo=utc)),
            preserve_default=False,
        ),
    ]