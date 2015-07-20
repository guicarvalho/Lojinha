# coding: utf-8

from django.db import models


class Promotion(models.Model):
    name = models.CharField(max_length=50)
    begin_date = models.DateField()
    end_date = models.DateField()
    percentage_discount = models.FloatField()
    visible = models.BooleanField()

    def __str__(self):
        return self.name


class PromotionProduct(models.Model):
    product = models.ForeignKey('product.Product')
    promotion = models.ForeignKey('Promotion')

    def __str__(self):
        return '{0} - {1} - {2}%%'.format(
            self.product.short_description,
            self.promotion.name,
            self.promotion.percentage_discount
            )
