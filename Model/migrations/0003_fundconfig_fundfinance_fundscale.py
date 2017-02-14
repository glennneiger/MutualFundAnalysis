# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0002_contact_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('totalass', models.FloatField()),
                ('stockinv', models.FloatField()),
                ('stockrat', models.FloatField()),
                ('bondcurr', models.FloatField()),
                ('bcrate', models.FloatField()),
                ('time', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FundFinance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('netincome', models.FloatField()),
                ('assincome', models.FloatField()),
                ('netassrate', models.FloatField()),
                ('netgrowrate', models.FloatField()),
                ('tonetgrora', models.FloatField()),
                ('time', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FundScale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('fundshare', models.FloatField()),
                ('netfunval', models.FloatField()),
                ('tolassfund', models.FloatField()),
                ('time', models.CharField(max_length=20)),
            ],
        ),
    ]
