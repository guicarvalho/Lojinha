# coding: utf-8

from django.db import models

from product.models import Product


class Cart(models.Model):
    """ Cart
        ~~~

    Shopping cart of e-commerce.
    """
    creation_date = models.DateField(auto_now_add=True)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    purchase_completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-creation_date']
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinhos'

    def __str__(self):
        return '{0}'.format(self.creation_date.strftime('%d-%m-%Y'))


class ItemCart(models.Model):
    """ ItemCart
        ~~~~~~~

    Store items of Shopping cart.
    """
    amount = models.IntegerField()
    has_discount = models.BooleanField(default=False)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cart = models.ForeignKey(Cart, related_name='cart_itens')
    product = models.ForeignKey(Product, related_name='itens')

    class Meta:
        ordering = ['cart']
        verbose_name = 'Item Carrinho'
        verbose_name_plural = 'Itens do Carrinho'

    def __str__(self):
        return '{0} {1}'.format(self.product.short_description, self.cart)
