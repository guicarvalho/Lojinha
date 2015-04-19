# coding: utf-8

from django import template

from product.models import Category

register = template.Library()


@register.assignment_tag
def list_categories():
    categories = Category.objects.all()
    return categories
