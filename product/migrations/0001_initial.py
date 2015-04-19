# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('color', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('long_description', models.TextField()),
                ('short_description', models.CharField(max_length=150)),
                ('min_stock', models.IntegerField()),
                ('max_stock', models.IntegerField()),
                ('sale_value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('production_value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('color', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
                ('publishing_date', models.DateTimeField(auto_now_add=True)),
                ('sku', models.CharField(unique=True, max_length=50)),
                ('category', models.ForeignKey(to='product.Category')),
            ],
            options={
                'ordering': ['-publishing_date'],
            },
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=160)),
                ('product', models.ForeignKey(to='product.Product')),
            ],
        ),
    ]
