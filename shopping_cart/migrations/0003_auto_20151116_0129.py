# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0002_auto_20151116_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='creation_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
