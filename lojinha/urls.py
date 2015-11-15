from django.conf.urls import include, url
from django.contrib import admin

from client.views import create_client
from product.views import (ProductCreateView, ProductDetailView, ProductListView,
                           ProductCategoryListView
                           )
from shopping_cart.views import Cart
from homepage.views import HomePageView
from core.views import login, logout


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

    # Category
    url(r'category/(?P<name>[-\w]+)/$', ProductCategoryListView.as_view(), name='category-list'),

    # Car
    url(r'car/add/', Cart.as_view(), name='cart-add'),

    # Client
    url(r'client/add/', create_client, name='client-add'),
]
