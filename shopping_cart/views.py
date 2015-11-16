# coding: utf-8

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import ugettext_lazy as _

from product.models import Product
from shopping_cart.models import Cart, ItemCart


def add_product(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if 'cart' not in request.session:
        cart = Cart()
        cart.save()
        request.session['cart'] = cart

    # if not _verificar_estoque_disponivel(request, produto_slug, quantidade):
    #    messages.error(request, 'Quantidade indisponível!')
    #    return redirect('detalhe_produto', produto_slug=produto_slug)

    cart = request.session.get('cart')

    item_in_cart = _find_product_in_cart(cart, product.slug)

    if not item_in_cart:
        cart_item = ItemCart()
        cart_item.product = product
        cart_item.cart = cart
        cart_item.amount = 1  # TODO: remove fixed amount
        cart_item.value = cart_item.amount * cart_item.product.sale_value
        cart_item.save()
        request.session['cart'] = cart
        messages.success(request, _('Produto adicionado no carrinho com sucesso!'))
    else:
        item = item_in_cart
        item.amount += 1  # TODO: remove fixed amount
        item.value = item.amount * item.product.sale_value
        item.save()
        messages.info(request, _('Produto atualizado com sucesso!'))

    _calculate_cart_value(request)

    return redirect('products-detail', slug=product.slug)


def _find_product_in_cart(cart, product_slug):
    product_list = list(filter(lambda x: x.product.slug == product_slug, cart.cart_itens.all()))
    product = None

    if product_list:
        product = product_list[0]

    return product


def _calculate_cart_value(request):
    cart = request.session.get('cart', Cart())

    value = sum([item.value for item in cart.cart_itens.all()])

    cart.total_value = value
    cart.save()

    request.session['cart'] = cart


def list_cart_itens(request):
    cart = request.session.get('cart', Cart())

    return render(request, 'shopping_cart/shopping_cart_list.html', {'cart': cart})
