from django.contrib import admin
from .models import Product, Brand, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'category', 'price', 'quantity')


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Category)
