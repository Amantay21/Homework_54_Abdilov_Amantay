from django import forms

from webapp.models import Category, Product, Cart, Order


class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'amount', 'image', 'category', 'qty']


class CartForms(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['product', 'qty']


class OrderForms(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'address', 'phone_number']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')
