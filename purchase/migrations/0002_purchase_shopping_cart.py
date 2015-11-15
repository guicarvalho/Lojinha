# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0001_initial'),
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='shopping_cart',
            field=models.ForeignKey(to='shopping_cart.Car'),
        ),
    ]
