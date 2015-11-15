# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_purchase_shopping_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('posting_date', models.DateField()),
                ('date_product_delivered', models.DateField(null=True, blank=True)),
                ('value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('purchase', models.ForeignKey(to='purchase.Purchase')),
            ],
        ),
    ]
