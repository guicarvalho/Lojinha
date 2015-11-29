# coding: utf-8

import locale

from django.template import Library

register = Library()


@register.filter
def get_range(value):
    return range(value)


@register.filter
def calculate_media(reviews):
    media = 0
    total = len(reviews)

    if not total:
        return 0

    for review in reviews:
        media += review.score

    return int(media / total)


@register.filter
def currency_format(value):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(float(value), grouping=True)
