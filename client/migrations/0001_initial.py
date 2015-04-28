# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('cpf_cnpj', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('cell_phone', models.CharField(max_length=11)),
                ('nickname', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
