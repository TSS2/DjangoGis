# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-25 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygis', '0007_auto_20180525_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysite_food',
            name='market',
            field=models.ManyToManyField(to='mygis.Mysite_Market'),
        ),
    ]
