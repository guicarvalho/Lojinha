# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_auto_20151116_0126'),
        ('product', '__first__'),
        ('shopping_cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('creation_date', models.DateField()),
                ('total_value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('purchase_completed', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Carrinhos',
                'verbose_name': 'Carrinho',
                'ordering': ['-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='ItemCart',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('has_discount', models.BooleanField()),
                ('discount_amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cart', models.ForeignKey(to='shopping_cart.Cart')),
                ('product', models.ForeignKey(to='product.Product', related_name='itens')),
            ],
            options={
                'verbose_name_plural': 'Itens do Carrinho',
                'verbose_name': 'Item Carrinho',
                'ordering': ['cart'],
            },
        ),
        migrations.RemoveField(
            model_name='itemcar',
            name='car',
        ),
        migrations.RemoveField(
            model_name='itemcar',
            name='product',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='ItemCar',
        ),
    ]
