from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product

def home_view(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {'products': products, 'categories': categories}

    return render(request, 'products/home.html', context)

def about_view(request):
    return render(request, 'products/about.html')

def contact_view(request):
    return render(request, 'products/contact.html')
