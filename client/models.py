# coding: utf-8

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Client(models.Model):
    """ Client
        ~~~~~~

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
    birthday = models.DateField()
    sex = models.CharField(max_length=1)

    def clean_sex(self):
        if self.sex not in ['M', 'F']:
            raise ValidationError(_(u'O sexo informado não é válido!'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def full_name(self):
        """ Returns first name and last name of client. """
        return '{0} {1}'.format(self.first_name, self.last_name)


class Address(models.Model):
    """ Address
        ~~~~~~~

    Address is a model of client address. It has OneToOne ralation with
    Client object.
    """
    street = models.CharField(max_length=70)
    number = models.IntegerField(validators=[
        MaxValueValidator(999999),
        MinValueValidator(0)
    ])
    complement = models.CharField(max_length=30, blank=True, null=True)
    neigthboor = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50, blank=True)
    client = models.OneToOneField(Client, related_name='address', blank=True)

    def __str__(self):
        return '{}, {}'.format(self.street, self.number)
