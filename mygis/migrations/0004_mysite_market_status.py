# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-08 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygis', '0003_mysite_market_data_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysite_market',
            name='status',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
