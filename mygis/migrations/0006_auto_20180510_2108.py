# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-10 13:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mygis', '0005_auto_20180510_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysite_asses',
            name='market_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mysite_market_mysite_asses', to='mygis.Mysite_Market'),
        ),
        migrations.AlterField(
            model_name='mysite_asses',
            name='message_person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_mysite_asses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mysite_peopletask',
            name='community_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Mysite_Community_mysite_peopletask', to='mygis.Mysite_Community'),
        ),
        migrations.AlterField(
            model_name='mysite_peopletask',
            name='data_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='mysite_peopletask',
            name='message_person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_mysite_peopletask', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mysite_pricetask',
            name='food_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mysite_food_mysite_pricetask', to='mygis.Mysite_Food'),
        ),
        migrations.AlterField(
            model_name='mysite_pricetask',
            name='market_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mysite_market_mysite_pricetask', to='mygis.Mysite_Market'),
        ),
        migrations.AlterField(
            model_name='mysite_pricetask',
            name='message_person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_mysite_pricetask', to=settings.AUTH_USER_MODEL),
        ),
    ]
