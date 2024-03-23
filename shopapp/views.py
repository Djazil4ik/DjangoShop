from django.shortcuts import render
from .models import Seller, Product
from django.contrib.auth.decorators import login_required

def catalog(request):
    Product.objects.all()
    product = Product.objects.filter().order_by('-datetime')
    return render(request, 'home.html', {'product': product})

def home(request):
    context = {}  # Empty context for now
    return render(request, 'home.html', context)

@login_required(login_url='/login')
def add_products(request):
    pass
