# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 19:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20160919_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='finish',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 20, 20, 45, 8, 261118, tzinfo=utc)),
        ),
    ]
