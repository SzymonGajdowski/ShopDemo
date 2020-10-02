from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import ProductForm, CategoryForm
from django.views.generic import DetailView

REDIRECT_URL = '/'

def home_view(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {'products': products, 'categories': categories,}

    return render(request, 'products/home.html', context)

def card_view(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {'products': products, 'categories': categories,}

    return render(request, 'products/card_view.html', context)

def about_view(request):
    return render(request, 'products/about.html')

def contact_view(request):
    return render(request, 'products/contact.html')

def categories_view(request):
    categories = Category.objects.all()

    context = {'categories': categories}

    return render(request, 'products/categories.html', context)

class ProductDetailView(DetailView):

    model = Product


# PRODUCT CRUD

def create_product(request):

    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(REDIRECT_URL)

    context = {'form': form}
    return render(request, 'products/create_form.html', context)

def edit_product(request, pk):

    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(REDIRECT_URL)

    context = {'form': form}
    return render(request, 'products/create_form.html', context)

def delete_product(request, pk):

    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect(REDIRECT_URL)

    return render(request, 'products/delete_form.html')

# CATEGORY CRUD

def create_category(request):

    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(REDIRECT_URL)

    context = {'form': form}
    return render(request, 'products/create_form.html', context)

def edit_category(request, pk):

    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect(REDIRECT_URL)

    context = {'form': form}
    return render(request, 'products/create_form.html', context)

def delete_category(request, pk):

    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect(REDIRECT_URL)

    return render(request, 'products/delete_form.html')

# User Registration and Login

def register_page(request):

    context = {}
    return render(request, 'products/register.html', context)

def login_page(request):

    context = {}
    return render(request, 'products/login.html', context)