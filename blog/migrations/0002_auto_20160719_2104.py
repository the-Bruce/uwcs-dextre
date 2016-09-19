# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='description',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='homepage',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sponsor_image',
            field=models.ForeignKey(blank=True, help_text='This image will be displayed in all sponsor display locations accross the website', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]
