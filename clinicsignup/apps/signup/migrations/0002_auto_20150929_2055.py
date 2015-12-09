# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='datetime',
            new_name='appointment_datetime',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='name',
            new_name='doctor_name',
        ),
    ]
