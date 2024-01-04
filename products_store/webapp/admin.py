from django.contrib import admin

from webapp.models import Product, Cart

admin.site.register(Product)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass
