# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_auto_20151125_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_datetime',
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointment_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
