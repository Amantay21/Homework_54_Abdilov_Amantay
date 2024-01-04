from django.db.models import F, Sum
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView

from webapp.forms import OrderForms
from webapp.models import Product, Cart, OrderProduct


class ProductAddToCart(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs['pk'])
        carts = Cart.objects.filter(product=product)
        if carts:
            cart = carts.first()
            if product.qty > cart.qty:
                cart.qty += 1
                cart.save()
        else:
            if product.qty > 0:
                Cart.objects.create(product=product, qty=1)
        return redirect('index')


class CartsView(TemplateView):
    template_name = 'carts/carts_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carts = Cart.objects.annotate(total=F('qty') * F('product__amount'))
        context['carts'] = carts
        context['total'] = carts.aggregate(total=Sum(F('qty') * F('product__amount')))['total']
        context['form'] = OrderForms()
        return context


class ProductCartDeleteFromCart(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Cart, product_id=kwargs['pk'])
        product.delete()
        return redirect('carts_list')


class OrderCreateView(CreateView):
    form_class = OrderForms

    def form_valid(self, form):
        order = form.save()
        carts = Cart.objects.all()
        for cart in carts:
            OrderProduct.objects.create(product=cart.product, order=order, qty=cart.qty)
        carts.delete()
        return redirect('index')
