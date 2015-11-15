# coding: utf-8

from django.db import models

from client.models import Client
from shopping_cart.models import Car


class PaymentType(models.Model):
    """ PaymentType
        ~~~~~~~~~~~

    Payment types.
    """
    name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)


class Purchase(models.Model):
    """ Purchase
        ~~~~~~~~

    Store information for a purchase.
    """
    shopping_cart = models.ForeignKey(Car)
    purchase_number = models.CharField(max_length=256)
    payment_type = models.ForeignKey(PaymentType)
    client = models.ForeignKey(Client, related_name='purchases')
