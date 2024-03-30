from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView
from django.contrib import messages
from .forms import ProductForm, SellerForm
from .models import Seller, Product
from django.contrib.auth import login, logout, authenticate


# Home page
def catalog(request):
    Product.objects.all()
    product = Product.objects.filter().order_by('-datetime')
    return render(request, 'catalog.html', {'product': product})

# Seller login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login the user if successful
            login(request, user)
            return redirect('/')  # Redirect to homepage after successful login
        else:
            # Authentication failed, display error message
            error_message = 'Invalid username or password.'
    else:
        # GET request, render the login form template
        error_message = None  # Clear any previous error messages for GET requests
    context = {'error_message': error_message, 'form': SellerForm}
    return render(request, 'shopapp/login.html', context)

# Sign Up
def SignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords does no match')
            return redirect('/')

        user = User.objects.create_user(username=username, password=password1)
        seller = Seller.objects.create(username=username)
        user.save()
        return redirect('login')
    form = UserCreationForm()
    return render(request, 'shopapp/signup.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    # Redirect to desired page after logout (e.g., login page)
    return redirect('catalog')

# Profile
def profile(request):
    seller = Seller.objects.get(pk=request.user.id)
    return render(request, 'profile.html', {'seller': seller})

# Product detail view
def detail_view(request, slug):
    product = Product.objects.filter(slug=slug).first()
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)

# Add product
@login_required(login_url='/login')
def add_product(request):
    if request.method == 'POST':
        seller = Seller.objects.filter(username=request.user).first()
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.seller = seller
            post.save()
            return redirect('/')
    else:
        form = ProductForm()
        return render(request, 'add_product.html', {'form': form})

# Delete product post
def Delete_Product(request, slug):
    products = Product.objects.get(slug=slug)
    if request.method == 'POST':
        products.delete()
        return redirect('/')
    return render(request, 'delete_product.html', {'products': products})

# Edit product post
def Update_Product(request, slug):
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})

def edit_seller_profile(request):
    seller = Seller.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = SellerForm(data=request.POST, files=request.FILES, instance=seller)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SellerForm(instance=seller)
    return render(request, 'edit_profile.html', {'form': form})