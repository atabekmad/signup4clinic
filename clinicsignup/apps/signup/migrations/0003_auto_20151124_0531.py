# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20150929_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorNames',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('patient_name', models.CharField(max_length=200)),
                ('appointment_datetime', models.DateTimeField(verbose_name="Appointment's date")),
            ],
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='doctor_name',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(to='signup.Doctor'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_name',
            field=models.ManyToManyField(to='signup.DoctorNames'),
        ),
    ]
