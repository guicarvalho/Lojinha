# coding: utf-8

from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
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
        product = context.get('object')

        context['product_details'] = product.productdetail_set.all()
        context['product_reviews'] = product.productreview_set.all()
        context['related_products'] = product.origin.all()
        return context


class ProductListView(ListView):
    model = Product


class ProductCategoryListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryListView, self).get_context_data(**kwargs)

        # get category name
        category_name = self.kwargs['name']
        object_list = Product.objects.filter(category__name__contains=category_name)

        context['object_list'] = object_list
        context['category'] = category_name

        return context
