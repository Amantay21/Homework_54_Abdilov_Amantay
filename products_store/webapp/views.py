from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import ProductForms
from webapp.models import Product, Category
from django.http import HttpResponseRedirect


def index_view(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'index.html', context)


def product_view(request, *args, pk, **kwargs):
    product = get_object_or_404(Product,  pk=pk)
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'products_view.html', {'product': product, 'category': category})


def delete_product(request):
    if request.method == "POST":
        product_id = request.POST.get('id')
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return redirect('index')


def create_product(request):
    if request.method == "GET":
        categories_product = Category.objects.all()
        products = Product.objects.all()
        return render(request, 'product_create.html', {'categories_product': categories_product, 'products': products})
    elif request.method == "POST":
        product = Product.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            created_at=request.POST.get('created_at'),
            amount=request.POST.get('amount'),
            image=request.POST.get('image'),
            category=Category(request.POST.get('category')))
        return redirect('product_view', pk=product.pk)


def create_category(request):
    if request.method == "GET":
        return render(request, 'category_create.html')
    elif request.method == "POST":
        category = Category.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description')
        )
        return redirect('index')

def category_view(request, *args, pk, **kwargs):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_view.html', {'category': category})

def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'product_delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('index')

def update_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        form = ProductForms(initial={
            'title': product.title,
            'amount': product.amount,
            'description': product.description,
            'image': product.image,
        })
        return render(request, 'product_update.html', {'form': form, 'product': product})
    elif request.method == "POST":
        form = ProductForms(data=request.POST)
        if form.is_valid():
            product.title = request.POST.get('title')
            product.amount = request.POST.get('amount')
            product.description = request.POST.get('description')
            product.image = request.POST.get('image')
            product.save()
            return redirect('index')
        else:
            return render(request, 'product_update.html', {'form': form})