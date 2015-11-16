# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0005_auto_20151116_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcart',
            name='cart',
            field=models.ForeignKey(related_name='cart_itens', to='shopping_cart.Cart'),
        ),
        migrations.AlterField(
            model_name='itemcart',
            name='discount_amount',
            field=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemcart',
            name='has_discount',
            field=models.BooleanField(default=False),
        ),
    ]
