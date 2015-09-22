# coding: utf-8

from django.db import models


class Client(models.Model):
    """ Client Model
        ~~~~~~~~~~~~

    Client is a model of clients of e-commerce. A client has address
    and your attributes.
    You can get fullname of instance of client call full_name method.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cpf_cnpj = models.CharField(max_length=14)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    cell_phone = models.CharField(max_length=11)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def full_name(self):
        """ Returns first name and last name of client. """
        return '{0} {1}'.format(self.first_name, self.last_name)


class Address(models.Model):
    """ Address model
        ~~~~~~~~~~~~~

    Address is a model of client address. It has OneToOne ralation with
    Client object.
    """
    street = models.CharField(max_length=70)
    number = models.IntegerField()
    complement = models.CharField(max_length=30, blank=True, null=True)
    neigthboor = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    client = models.OneToOneField(Client)

    def __str__(self):
        return '{}, {}'.format(self.street, self.number)
