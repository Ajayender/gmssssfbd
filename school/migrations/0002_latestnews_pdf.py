# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-04 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='latestnews',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
