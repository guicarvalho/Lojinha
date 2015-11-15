# coding: utf-8

from django.db import models

from purchase.models import Purchase


class Delivery(models.Model):
    """ Delivery
        ~~~~~~~~

    Stores the delivery information.
    """
    posting_date = models.DateField()
    date_product_delivered = models.DateField(null=True, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    purchase = models.ForeignKey(Purchase)

    def __str__(self):
        return self.posting_date
