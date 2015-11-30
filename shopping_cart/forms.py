# coding: utf-8

from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator


class CartForm(forms.Form):
    amount = forms.IntegerField(validators=[MaxLengthValidator(99), MinLengthValidator(1)])
