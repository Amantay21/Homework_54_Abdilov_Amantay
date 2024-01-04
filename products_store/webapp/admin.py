from django.contrib import admin

from webapp.models import Product, Cart, OrderProduct, Order

admin.site.register(Product)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class CartAdmin(admin.ModelAdmin):
    pass
@admin.register(OrderProduct)
class CartAdmin(admin.ModelAdmin):
    pass
