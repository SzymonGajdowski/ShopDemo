from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import ProductForm, CategoryForm, CreateUserForm
from django.views.generic import DetailView

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


REDIRECT_URL = '/'

def home_view(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    search = request.GET.get('search')
    if search:
        q1 = Product.objects.filter(name__contains=search)
        products = q1
    context = {'products': products, 'categories': categories}

    return render(request, 'products/home.html', context)

def card_view(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    search = request.GET.get('search')
    if search:
        q1 = Product.objects.filter(name__contains=search)
        products = q1
    context = {'products': products, 'categories': categories}

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
@login_required
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
@login_required
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

    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created')
            return redirect('login')
    context = {'form': form}
    return render(request, 'products/register.html', context)
