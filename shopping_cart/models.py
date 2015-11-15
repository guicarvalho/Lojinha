# coding: utf-8

from django.db import models

from product.models import Product


class Car(models.Model):
    """ Car
        ~~~

    Shopping cart of e-commerce.
    """
    creation_date = models.DateField()
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_completed = models.BooleanField()

    class Meta:
        ordering = ['-creation_date']
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinhos'

    def __str__(self):
        return '{0}'.format(self.creation_date.strftime('%d-%m-%Y'))


class ItemCar(models.Model):
    """ ItemCar
        ~~~~~~~

    Store items of Shopping car.
    """
    amount = models.IntegerField()
    has_discount = models.BooleanField()
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    car = models.ForeignKey(Car)
    product = models.ForeignKey(Product, related_name='itens')

    class Meta:
        ordering = ['car']
        verbose_name = 'Item Carrinho'
        verbose_name_plural = 'Itens do Carrinho'

    def __str__(self):
        return '{0} {1}'.format(self.product.short_description, self.car)
