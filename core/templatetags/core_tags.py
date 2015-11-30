# coding: utf-8

import locale

from django.template import Library

register = Library()


@register.filter
def currency_format(value):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(float(value or 0), grouping=True)
