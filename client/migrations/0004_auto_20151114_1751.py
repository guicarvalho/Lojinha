# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20151108_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='sex',
            field=models.CharField(max_length=1, default=datetime.datetime(2015, 11, 14, 17, 51, 16, 938047, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='complement',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='neigthboor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(max_length=10),
        ),
    ]
