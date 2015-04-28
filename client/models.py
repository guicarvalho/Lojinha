# coding: utf-8

from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cpf_cnpj = models.CharField(max_length=14)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    cell_phone = models.CharField(max_length=11)
    nickname = models.CharField(max_length=50)
    photo = models.ImageField()

    def __unicode__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
