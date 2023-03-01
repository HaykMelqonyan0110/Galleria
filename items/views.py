from django.shortcuts import render
from .models import Category, Subcategory, Product

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'home.html', {'categories': categories, 'products': products})

def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    subcategories = category.subcategory_set.all()
    return render(request, 'category_detail.html', {'category': category, 'subcategories': subcategories})

def subcategory_detail(request, pk):
    subcategory = Subcategory.objects.get(pk=pk)
    products = subcategory.product_set.all()
    return render(request, 'subcategory_detail.html', {'subcategory': subcategory, 'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})

