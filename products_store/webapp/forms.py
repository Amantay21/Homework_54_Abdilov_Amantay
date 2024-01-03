from django import forms

from webapp.models import Category, Product


class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'amount', 'image', 'category']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')
