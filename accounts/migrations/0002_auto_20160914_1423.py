# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 14:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databaseaccount',
            name='name',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=re.compile('[^a-z0-9]', 32))]),
        ),
        migrations.AlterField(
            model_name='shellaccount',
            name='name',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=re.compile('[^a-z0-9]', 32))]),
        ),
    ]