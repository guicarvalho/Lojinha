# coding: utf-8

from datetime import datetime

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
    sku = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey('Category')

    class Meta:
        ordering = ['-publishing_date']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return '{0}. {1}'.format(self.sku, self.short_description)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug', self.slug})


class Category(models.Model):
    name = models.CharField(max_length=60)
    color = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return '{0}'.format(self.name)


class ProductDetail(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=160)
    product = models.ForeignKey('Product')

    class Meta:
        ordering = ['name']
        verbose_name = 'Detalhe Produto'
        verbose_name_plural = 'Detalhes Produto'

    def __str__(self):
        return '{0}.{1}: {2}'.format(
            self.product.sku,
            self.product.short_description,
            self.name
            )


class ProductReview(models.Model):
    score = models.IntegerField()
    pros = models.CharField(max_length=350)
    cons = models.CharField(max_length=350)
    opinion = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)
    visible = models.BooleanField()
    product = models.ForeignKey('Product')
    client = models.ForeignKey('client.Client')

    class Meta:
        ordering = ['-creation_date']
        verbose_name = 'Revisão Produto'
        verbose_name_plural = 'Revisões Produto'

    def __str__(self):
        return 'SKU {0} ({1}): {2} [{3}]'.format(
            self.product.sku,
            self.product.short_description,
            self.client,
            datetime.strftime(self.creation_date, '%d-%m-%Y')
            )


class RelatedProduct(models.Model):
    product_origin = models.ForeignKey('Product', related_name='origin')
    related_product = models.ForeignKey('Product', related_name='related')

    class Meta:
        verbose_name = 'Produto Relacionado'
        verbose_name_plural = 'Produtos Relacionados'

    def __str__(self):
        return '{0} : {1}'.format(self.product_one.name, self.product_two.name)
