from django.db import models

from django.shortcuts import render

from django.db import models


class Category(models.Model):
    title = models.TextField(max_length=200, null=False, blank=False, verbose_name='Название', unique=True)
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.id}. {self.title}'


class Product(models.Model):
    title = models.TextField(max_length=200, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name="Цена")
    image = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey('webapp.Category',
                             on_delete=models.RESTRICT,
                             verbose_name='Категория',
                             related_name='categories',
                             null=True)

    def __str__(self):
        return f'{self.id}. {self.title}'
