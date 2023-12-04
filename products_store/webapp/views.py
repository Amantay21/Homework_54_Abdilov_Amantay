from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.models import Product, Category
from django.http import HttpResponseRedirect


def index_view(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'index.html', context)


def product_view(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products_view.html', {'product': product})


def delete_product(request):
    if request.method == "POST":
        product_id = request.POST.get('id')
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return redirect('index')


def create_product(request):
    if request.method == "GET":
        return render(request, 'product_create.html')
    elif request.method == "POST":
        product = Product.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            created_at=request.POST.get('created_at'),
            amount=request.POST.get('amount'),
            image=request.POST.get('image'),
            category=request.POST.get('category'))
        return redirect('product_view', pk=product.pk)


def create_category(request):
    print("111111111111111111111111111")
    if request.method == "GET":
        return render(request, 'category_create.html')
    elif request.method == "POST":
        category = Category.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description')
        )
        print(category+"============================")
        return redirect('index', pk=category.pk)
