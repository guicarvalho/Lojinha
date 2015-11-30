from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from client.views import create_client
from core.views import login, logout
from homepage.views import HomePageView
from product.views import (ProductCreateView, ProductDetailView, ProductListView,
                           ProductCategoryListView, product_detail_json
                           )
from purchase.views import CheckoutView
from shopping_cart.views import add_product, list_cart_itens, calculate_delivery, remove_item_cart, update_cart
from wishlist.views import WishListListView, WishListDeleteView, WishListItemDeleteView, add_item_wishlist


urlpatterns = [
    # url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', HomePageView.as_view(), name='home_page'),

    url(r'login/$', login, name='login'),
    url(r'logout/$', logout, name='logout'),

    # Products
    url(r'products/$', ProductListView.as_view(), name='products-list'),
    url(r'products/add/$', ProductCreateView.as_view(), name='products-add'),
    url(r'products/(?P<slug>[-_\w]+)/$', ProductDetailView.as_view(), name='products-detail'),
    url(r'products/json/(?P<slug>[-_\w]+)/$', product_detail_json, name='products-detail-json'),

    # Category
    url(r'category/(?P<name>[-\w]+)/$', ProductCategoryListView.as_view(), name='category-list'),

    # Cart
    url(r'cart/add/(?P<slug>[-_\w]+)/$', add_product, name='cart-add'),
    url(r'cart/list/$', list_cart_itens, name='cart-list'),
    url(r'cart/calculateDelivery/(?P<zip_code>[-\d]+)/$', calculate_delivery, name='cart-calculate-delivery'),
    url(r'cart/remove/(?P<pk>\d+)/', remove_item_cart, name='cartitem-delete'),
    url(r'cart/update/', update_cart, name='update-cart'),

    # Purchase
    url(r'checkout/$', CheckoutView.as_view(), name='purchase-checkout'),

    # Client
    url(r'client/add/', create_client, name='client-add'),

    # Wishlist
    url(r'whishlist/add/(?P<slug>[-\w]+)/$', add_item_wishlist, name='whishlist-add'),
    url(r'whishlist/$', WishListListView.as_view(), name='whishlist-list'),
    url(r'whishlist/remove/(?P<pk>\d+)/', WishListItemDeleteView.as_view(), name='wishlistitem-delete'),
    url(r'whishlist/clean/(?P<pk>\d+)/', WishListDeleteView.as_view(), name='wishlist-delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
