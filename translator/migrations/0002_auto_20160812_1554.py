# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translatedtext',
            name='translate_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date translated'),
        ),
    ]
