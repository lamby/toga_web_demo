# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160310155155 on 2016-03-11 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]