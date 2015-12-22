# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_auto_20151220_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateField(null=True, blank=True, verbose_name="Appointment's date"),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.TimeField(null=True, blank=True, verbose_name="Appointment's time"),
        ),
    ]
