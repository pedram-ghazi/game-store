# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-22 12:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_auto_20170421_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paymentDate',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]