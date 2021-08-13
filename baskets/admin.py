from django.contrib import admin

from baskets.models import Basket
from products.models import ProductCategory

# admin.site.register(Basket)
# admin.site.register(ProductCategory)


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
    readonly_fields = ('user',)
    ordering = ('-user',)
    search_fields = ('user',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    ordering = ('-name',)
    search_fields = ('name',)