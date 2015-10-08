# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emp_id', models.IntegerField(default=0)),
                ('emp_firstname', models.CharField(max_length=50)),
                ('emp_lastname', models.CharField(max_length=50)),
                ('emp_salary', models.FloatField()),
                ('emp_doj', models.DateTimeField()),
                ('emp_email', models.EmailField(max_length=255)),
                ('emp_phoneno', models.CharField(max_length=20, blank=True)),
            ],
        ),
    ]
