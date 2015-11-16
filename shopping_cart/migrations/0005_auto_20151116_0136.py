# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0004_auto_20151116_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='purchase_completed',
            field=models.BooleanField(default=False),
        ),
    ]
