# coding: utf-8

from django.http import Http404
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView

from client.models import Client
from product.models import Product, ProductTag
from wishlist.models import WishList, WishListItem


class WishListListView(ListView):
    model = WishList
    context_object_name = 'wishlist'

    def get_context_data(self, **kwargs):
        ctx = super(WishListListView, self).get_context_data(**kwargs)
        return ctx


class WishListDeleteView(DeleteView):
    model = WishList
    success_url = reverse_lazy('whishlist-list')

    def get_object(self, query_set=None):
        wishlist = super(WishListDeleteView, self).get_object()

        wishlist_items = wishlist.wishlist_items.all()

        ctx = {'object_list': wishlist_items}

        return ctx

    def delete(self, *args, **kwargs):
        wishlist_id = self.kwargs['pk']

        items = WishListItem.objects.filter(wishlist__id=wishlist_id).all()
        items.delete()

        return redirect(reverse('whishlist-list'))


class WishListItemDeleteView(DeleteView):
    model = WishListItem
    success_url = reverse_lazy('whishlist-list')


@login_required
def add_item_wishlist(request, slug):
    client = Client.objects.filter(email=request.user.username).first()

    wishlist = WishList.objects.get_or_create(client=client)

    if isinstance(wishlist, tuple):
        wishlist = wishlist[0]

    product = get_object_or_404(Product, slug=slug)

    product_already_wishlist = wishlist.wishlist_items.filter(product=product).exists()

    if not product_already_wishlist:
        wishlist_item = WishListItem(wishlist=wishlist, product=product)
        wishlist_item.save()

        messages.info(request, _(u'Produto adicionado a lista de desejos !'))
    else:
        messages.info(request, _(u'O produto {0} já se encontra na sua lista de desejos !'
                                 '  <a class="pull-right" href={1}>Veja sua lista de desejos</a>'
                                 .format(product.short_description, reverse('whishlist-list'))))

    return redirect('products-detail', slug=product.slug)
