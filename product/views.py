# coding: utf-8

from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from product.models import Product, ProductTag


def product_detail_json(request, slug):
    product = get_object_or_404(Product, slug=slug)

    product_dict = model_to_dict(product)
    product_dict['main_image'] = product.product_images.first().image_path.url
    product_dict['list_images'] = [img.image_path.url for img in product.product_images.all()]
    product_dict['short_description'] = product.short_description.title()

    print (product_dict['list_images'])

    return JsonResponse(product_dict)


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

        # get product tags
        product.tags = ProductTag.objects.filter(products__in=[product])

        context['product_details'] = product.product_details.all()
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
        product_list = Product.objects.filter(category__name__contains=category_name)

        # get tags
        tag_list = ProductTag.objects.filter(name=category_name)

        object_list = []

        for item in tag_list:
            for p in item.products.all():
                object_list.append(p)

        for item in product_list:
            object_list.append(item)

        context['object_list'] = object_list
        context['category'] = category_name

        return context
