from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Product
from .forms import ProductForm

def home_view(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {'products': products, 'categories': categories}

    return render(request, 'products/home.html', context)

def about_view(request):
    return render(request, 'products/about.html')

def contact_view(request):
    return render(request, 'products/contact.html')

def create_product(request):

    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'products/create_form.html', context)

def edit_product(request, pk):

    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'products/create_form.html', context)

def delete_product(request, pk):

    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/')

    return render(request, 'products/delete_form.html')