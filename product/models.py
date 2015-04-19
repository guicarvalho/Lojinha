# coding: utf-8

from django.core.urlresolvers import reverse
from django.db import models


class Product(models.Model):
    long_description = models.TextField()
    short_description = models.CharField(max_length=150)
    min_stock = models.IntegerField()
    max_stock = models.IntegerField()
    sale_value = models.DecimalField(max_digits=10, decimal_places=2)
    production_value = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=30)
    slug = models.SlugField()
    publishing_date = models.DateTimeField(auto_now_add=True)
    sku = models.CharField(max_length=50, unique=True)  # unique product identifier
    category = models.ForeignKey('Category')

    class Meta:
        ordering = ['-publishing_date']

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug', self.slug})


class Category(models.Model):
    name = models.CharField(max_length=60)
    color = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']


class ProductDetail(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=160)
    product = models.ForeignKey('Product')

    ordering = ['name']
