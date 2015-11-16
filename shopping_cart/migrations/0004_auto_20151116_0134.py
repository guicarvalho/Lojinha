# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0003_auto_20151116_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_value',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
    ]
