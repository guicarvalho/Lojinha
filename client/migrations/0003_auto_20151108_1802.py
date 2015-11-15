# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20150922_0402'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2015, 11, 8, 18, 2, 6, 968479, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='address',
            name='client',
            field=models.OneToOneField(related_name='address', to='client.Client'),
        ),
        migrations.AlterField(
            model_name='address',
            name='complement',
            field=models.CharField(max_length=30, blank=True, null=True, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=50, verbose_name='País'),
        ),
        migrations.AlterField(
            model_name='address',
            name='neigthboor',
            field=models.CharField(max_length=50, verbose_name='Logradouro'),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.IntegerField(verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=2, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=70, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(max_length=10, verbose_name='CEP'),
        ),
    ]
