# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_auto_20151124_0531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('patient_first_name', models.CharField(max_length=200)),
                ('patient_last_name', models.CharField(max_length=200)),
                ('patient_middle_name', models.CharField(max_length=200)),
                ('appointment_datetime', models.DateTimeField(verbose_name="Appointment's date")),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='doctor_name',
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_full_name',
            field=models.CharField(max_length=200, default='Xren Dmitriy Nikolaevich'),
        ),
        migrations.DeleteModel(
            name='DoctorNames',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(to='signup.Doctor'),
        ),
    ]
