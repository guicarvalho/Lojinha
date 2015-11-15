# coding: utf-8

from django.contrib import admin

from product.models import Product, Category, ProductDetail, ProductReview, RelatedProduct, ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductDetail)
class ProductDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(RelatedProduct)
class RelatedProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass
