# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-16 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='http_header',
            field=models.TextField(default='', verbose_name='httpHeader'),
            preserve_default=False,
        ),
    ]
