from django.urls import path

from webapp.views.cart_views import ProductAddToCart, ProductCartDeleteFromCart, CartsView, OrderCreateView
from webapp.views.product_views import ProductsView, ProductCreateView, ProductDetailView, \
    ProductUpdateView, ProductDeleteView
from webapp.views.category_views import CategoryView, CategoryCreateView





urlpatterns = [
    path('', ProductsView.as_view(), name='index'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='products_view'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>', CategoryView.as_view(), name='category_view'),
    path('product/<int:pk>/add_to_cart/', ProductAddToCart.as_view(), name='product_add_to_cart_view'),
    path('carts/', CartsView.as_view(), name='carts_list'),
    path('products/<int:pk>/delete_from_cart', ProductCartDeleteFromCart.as_view(),
         name='product_delete_from_cart_view'),
    path('order/add/', OrderCreateView.as_view(), name='order_add_view')
]
