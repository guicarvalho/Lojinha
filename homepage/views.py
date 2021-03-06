# coding: utf-8

from django.views.generic.base import TemplateView

from core.forms import LoginForm
from product.models import Product


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['recent_products'] = self._get_recent_products()
        context['login_form'] = LoginForm()
        return context

    def _get_recent_products(self):
        """
        Get last five products registered in db.
        """
        products = Product.objects.order_by('-publishing_date')[:5]
        return products
