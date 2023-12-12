from django.urls import path
from webapp.views import index_view, delete_product, create_product, product_view, create_category, category_view, \
    product_delete_view, update_product_view

urlpatterns = [
    path('', index_view, name='index'),
    path('product/add/', create_product, name='product_create'),
    path('product/<int:pk>', product_view, name='product_view'),
    path('product/delete/', delete_product, name='delete_product'),
    path('category/add/', create_category, name='category_create'),
    path('category/<int:pk>', category_view, name='category_view'),
    path('product/<int:pk>/delete', product_delete_view, name='product_delete'),
    path('product/<int:pk>/update', update_product_view, name='product_update'),
]