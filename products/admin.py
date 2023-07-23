from django.contrib import admin

from products.models import ProductCategory, Product

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)