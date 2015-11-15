# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('creation_date', models.DateField()),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_completed', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Carrinhos',
                'verbose_name': 'Carrinho',
                'ordering': ['-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='ItemCar',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('amount', models.IntegerField()),
                ('has_discount', models.BooleanField()),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('car', models.ForeignKey(to='shopping_cart.Car')),
                ('product', models.ForeignKey(to='product.Product', related_name='itens')),
            ],
            options={
                'verbose_name_plural': 'Itens do Carrinho',
                'verbose_name': 'Item Carrinho',
                'ordering': ['car'],
            },
        ),
    ]
