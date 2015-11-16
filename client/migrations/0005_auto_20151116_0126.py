# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20151114_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='client',
            field=models.OneToOneField(to='client.Client', blank=True, related_name='address'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='birthday',
            field=models.DateField(),
        ),
    ]
