# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-11 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160811_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogarticle',
            name='is_puplished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blogarticle',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]