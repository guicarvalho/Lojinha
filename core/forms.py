# coding: utf-8

from django import forms
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(label=_('Usuário'), required=True, max_length=254,
                               widget=forms.TextInput(attrs={'class': 'form-control input_md'}))
    password = forms.CharField(label=_('Senha'), required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control input_md'}))
