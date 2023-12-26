from django import forms

from webapp.models import Category


class ProductForms(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Название')
    description = forms.EmailField(max_length=400, required=True, label='Описание')
    amount = forms.DecimalField(max_digits=7, decimal_places=2, required=True, label="Цена")
    image = forms.CharField(max_length=5000, required=True, label='Изображение')
    category = forms.ModelChoiceField(queryset=Category.objects.all())