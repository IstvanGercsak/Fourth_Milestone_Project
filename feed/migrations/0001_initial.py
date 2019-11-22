# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-22 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('images', models.ImageField(upload_to='images')),
            ],
        ),
    ]