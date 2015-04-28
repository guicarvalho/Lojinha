# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productreview_relatedproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('percentage_discount', models.FloatField()),
                ('visible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='PromotionProduct',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('product', models.ForeignKey(to='product.Product')),
                ('promotion', models.ForeignKey(to='promotion.Promotion')),
            ],
        ),
    ]
