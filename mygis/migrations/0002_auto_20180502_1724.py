# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-02 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysite_asses',
            name='asses_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mysite_community',
            name='community_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mysite_datatime',
            name='data_time_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mysite_food',
            name='food_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mysite_market',
            name='market_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mysite_peopletask',
            name='task_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mysite_pricetask',
            name='task_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mysite_restaurant',
            name='restaurant_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mysite_store',
            name='store_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mysite_target',
            name='target_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
