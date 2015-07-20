# coding: utf-8

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
