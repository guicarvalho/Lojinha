# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('score', models.IntegerField()),
                ('pros', models.CharField(max_length=350)),
                ('cons', models.CharField(max_length=350)),
                ('opinion', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('visible', models.BooleanField()),
                ('client', models.ForeignKey(to='client.Client')),
                ('product', models.ForeignKey(to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='RelatedProduct',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('product_origin', models.ForeignKey(to='product.Product', related_name='origin')),
                ('related_product', models.ForeignKey(to='product.Product', related_name='related')),
            ],
        ),
    ]
