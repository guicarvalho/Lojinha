# coding: utf-8

from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator

from product.models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'

    @method_decorator(login_required)
    def form_valid(self, form):
        # form.instance.created_by = self.request.user
        return super(ProductCreateView, self).form_valid(form)


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        return context
