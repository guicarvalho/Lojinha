# coding: utf-8

# from django.contrib.auth.decorators import login_required

from django.views.generic.base import TemplateView

# from django.utils.decorators import method_decorator

from product.models import Product


class HomePageView(TemplateView):
    template_name = 'home.html'

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(HomePageView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['recent_products'] = self._get_recent_products()
        return context

    def _get_recent_products(self):
        """
        Get last five products registered in db.
        """
        products = Product.objects.order_by('-publishing_date')[:5]
        return products
