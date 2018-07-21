# Generated by Django 2.0.7 on 2018-07-21 08:14

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20180720_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='spacebucks',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doorlog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]