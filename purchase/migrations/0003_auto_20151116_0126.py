# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_purchase_shopping_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='shopping_cart',
            field=models.ForeignKey(to='shopping_cart.Cart'),
        ),
    ]
