# Generated by Django 3.0.8 on 2020-07-29 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('events', '0003_auto_20200725_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtype',
            name='list_image',
            field=models.ForeignKey(blank=True, help_text='This image will be displayed above the event on the front page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]