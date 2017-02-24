# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0013_mutualfundmanagerinfo_managerid'),
    ]

    operations = [
        migrations.CreateModel(
            name='MutualFundManagerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.CharField(max_length=200)),
                ('managerId', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('manageStart', models.CharField(max_length=200)),
                ('manageStartDate', models.DateField()),
                ('manageLength', models.IntegerField()),
                ('manageEnd', models.CharField(max_length=200)),
                ('manageEndDate', models.DateField()),
                ('length', models.IntegerField()),
                ('onPosition', models.IntegerField()),
                ('manageAchive', models.FloatField()),
                ('manageAvgAchive', models.FloatField()),
                ('updateDate', models.CharField(max_length=200)),
            ],
        ),
    ]
