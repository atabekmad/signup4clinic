# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('datetime', models.DateTimeField(verbose_name="Appointment's date")),
                ('patient_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(to='signup.Doctor'),
        ),
    ]
