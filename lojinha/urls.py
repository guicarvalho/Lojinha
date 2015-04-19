from django.conf.urls import include, url
from django.contrib import admin

from product.views import ProductCreateView, ProductDetailView
from homepage.views import HomePageView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', HomePageView.as_view(), name='home_page'),

    # products
    url(r'product/add/$', ProductCreateView.as_view(), name='product-add'),
    url(
        r'product/(?P<slug>[-_\w]+)/$',
        ProductDetailView.as_view(),
        name='product-detail'
        ),
]
