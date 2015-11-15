# coding: utf-8

from django.db import models

from client.models import Client
from product.models import Product


class WishList(models.Model):
    """ WishList
        ~~~~~~~~

    Stores the products you would like to buy future.
    """
    client = models.ForeignKey(Client)

    def __str__(self):
        return 'WishList - Client {}'.format(self.client.id)


class WishListItem(models.Model):
    """ WishListItem
        ~~~~~~~~~~~~

    Is the items in the wishlist.
    """
    wishlist = models.ForeignKey(WishList, related_name='wishlist_items')
    product = models.ForeignKey(Product)

    def __str__(self):
        return 'WishListItem - Product {}'.format(self.product.id)
