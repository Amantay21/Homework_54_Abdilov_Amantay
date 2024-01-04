from django.db import models

from django.shortcuts import render

from django.db import models


class Category(models.Model):
    title = models.TextField(max_length=200, null=False, blank=False, verbose_name='Название', unique=True)
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.id}. {self.title}'


class Product(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=9000, null=True, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name="Цена")
    image = models.CharField(max_length=9000, null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey('webapp.Category',
                                 on_delete=models.RESTRICT,
                                 verbose_name='Категория',
                                 related_name='categories',
                                 null=True)
    qty = models.PositiveIntegerField(default=1, verbose_name='Остаток')

    def __str__(self):
        return f'{self.id}. {self.title}'


class Cart(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='products',
                                verbose_name='Продукт')
    qty = models.PositiveIntegerField(default=0, verbose_name='Количество')


class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя заказчика')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    phone_number = models.CharField(max_length=100, verbose_name='Телефон')
    сreated_at = models.DateTimeField(auto_now_add=True, verbose_name='Время обновления')
    products = models.ManyToManyField('webapp.Product', related_name='orders', through='webapp.OrderProduct'
                                      , through_fields=('order', 'product'), verbose_name='Продукты')
    def __str__(self):
        return f'{self.id}. {self.name}  {self.phone_number} '
class OrderProduct(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='product_orders')
    order = models.ForeignKey('webapp.Order', on_delete=models.CASCADE, related_name='order_products')
    qty = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{self.id}. {self.product}, {self.order}, {self.qty}'