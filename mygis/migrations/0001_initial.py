# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-01 08:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mysite_Asses',
            fields=[
                ('asses_id', models.IntegerField(primary_key=True, serialize=False)),
                ('asses_comment', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mysite_Community',
            fields=[
                ('community_id', models.IntegerField(primary_key=True, serialize=False)),
                ('community_name', models.CharField(max_length=100)),
                ('community_address', models.CharField(max_length=100)),
                ('community_long', models.CharField(max_length=100)),
                ('community_dimen', models.CharField(max_length=100)),
                ('community_wyphone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mysite_DataTime',
            fields=[
                ('data_time_id', models.IntegerField(primary_key=True, serialize=False)),
                ('data_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Mysite_Food',
            fields=[
                ('food_id', models.IntegerField(primary_key=True, serialize=False)),
                ('food_name', models.CharField(max_length=100)),
                ('food_kind', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mysite_Market',
            fields=[
                ('market_id', models.IntegerField(primary_key=True, serialize=False)),
                ('market_name', models.CharField(max_length=100)),
                ('market_address', models.CharField(max_length=100)),
                ('market_long', models.CharField(max_length=100)),
                ('market_dimen', models.CharField(max_length=100)),
                ('market_phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mysite_PeopleTask',
            fields=[
                ('task_id', models.IntegerField(primary_key=True, serialize=False)),
                ('num_people', models.IntegerField()),
                ('community_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygis.Mysite_Community')),
                ('data_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygis.Mysite_DataTime')),
                ('message_person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mysite_PriceTask',
            fields=[
                ('task_id', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.CharField(max_length=50)),
                ('data_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygis.Mysite_DataTime')),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygis.Mysite_Food')),
                ('market_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygis.Mysite_Market')),
                ('message_person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mysite_Restaurant',
            fields=[
                ('restaurant_id', models.IntegerField(primary_key=True, serialize=False)),
                ('restaurant_name', models.CharField(max_length=100)),
                ('restaurant_address', models.CharField(max_length=100)),
                ('restaurant_long', models.CharField(max_length=100)),
                ('restaurant_dimen', models.CharField(max_length=100)),
                ('restaurant_wyphone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mysite_Store',
            fields=[
                ('store_id', models.IntegerField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=100)),
                ('store_address', models.CharField(max_length=100)),
                ('store_long', models.CharField(max_length=100)),
                ('store_dimen', models.CharField(max_length=100)),
                ('store_wyphone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mysite_Target',
            fields=[
                ('target_id', models.IntegerField(primary_key=True, serialize=False)),
                ('lrzw', models.CharField(max_length=100)),
                ('twzj', models.CharField(max_length=100)),
                ('cyryywzj', models.CharField(max_length=100)),
                ('csws', models.CharField(max_length=100)),
                ('xfws', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='mysite_asses',
            name='market_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygis.Mysite_Market'),
        ),
        migrations.AddField(
            model_name='mysite_asses',
            name='message_person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
