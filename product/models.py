# coding: utf-8

from datetime import datetime

from django.core.urlresolvers import reverse
from django.db import models


class Product(models.Model):
    """ Product
        ~~~~~~~

    Product is a model of products of e-commerce. A product has category
    and your attributes.
    The products are ordering by publishing_date.
    """
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
    category = models.ForeignKey('Category', related_name='products')

    class Meta:
        ordering = ['-publishing_date']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return '{}. {}'.format(self.sku, self.short_description)

    def get_absolute_url(self):
        return reverse('products-detail', kwargs={'slug', self.slug})


class Category(models.Model):
    """ Category
        ~~~~~~~~

    Category is a model of category of product. The categories are ordering by name.
    """
    name = models.CharField(max_length=60)
    color = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return '{}'.format(self.name)


class ProductDetail(models.Model):
    """ ProductDetail
        ~~~~~~~~~~~~~

    Product Detail are related with Product 1:N. All details
    of products when not are presents in product model are
    stored here in key -> value format. Example:

    material -> plastic
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=160)
    product = models.ForeignKey('Product', related_name='product_details')

    class Meta:
        ordering = ['name']
        verbose_name = 'Detalhe Produto'
        verbose_name_plural = 'Detalhes Produto'

    def __str__(self):
        return '{}.{}: {}'.format(
            self.product.sku,
            self.product.short_description,
            self.name
            )


class ProductReview(models.Model):
    """ ProductReview
        ~~~~~~~~~~~~~

    Store all products reviews, by default reviews dont appear in
    web site without permission of system administrator.
    """
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
        return 'SKU {} ({}): {} [{}]'.format(
            self.product.sku,
            self.product.short_description,
            self.client,
            datetime.strftime(self.creation_date, '%d-%m-%Y')
            )


class RelatedProduct(models.Model):
    """ RelatedProduct
        ~~~~~~~~~~~~~~

    Store related products.
    """
    product_origin = models.ForeignKey('Product', related_name='origin')
    related_product = models.ForeignKey('Product', related_name='related')

    class Meta:
        verbose_name = 'Produto Relacionado'
        verbose_name_plural = 'Produtos Relacionados'

    def __str__(self):
        return '{} : {}'.format(self.product_origin.short_description, self.related_product.short_description)


class ProductImage(models.Model):
    """ ProductImage
        ~~~~~~~~~~~~

    Store all product images.
    """
    image_path = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product, related_name='product_images')

    def __str__(self):
        return '{}: {} <{}>'.format(self.id, self.product.short_description, self.image_path.url)


class ProductTag(models.Model):
    """ ProductTag
        ~~~~~~~~~~

    Store all product tags.
    """
    name = models.CharField(max_length=40)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)
