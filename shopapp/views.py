from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import messages
from .forms import ProductForm, SellerForm
from .models import Seller, Product
from django.contrib.auth import login, logout

def catalog(request):
    Product.objects.all()
    product = Product.objects.filter().order_by('-datetime')
    return render(request, 'catalog.html', {'product': product})

def home(request):
    context = {}  # Empty context for now
    return render(request, 'home.html', context)

class SellerLoginView(LoginView):
    template_name = 'shopapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

def SignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords does no match')
            return reverse_lazy('home')

        user = User.objects.create_user(username, password1)
        user.save()
        return render(request, 'shopapp/login.html')
    form = UserCreationForm()
    return render(request, 'shopapp/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    # Redirect to desired page after logout (e.g., login page)
    return redirect('home')

def profile(request):
    return render(request, 'profile.html')

def detail_view(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)

@login_required(login_url='/login')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.seller = request.user
            post.save()
            obj = form.instance
            alert = True
            return render(request, 'add_product.html', {'obj': obj, 'alert': alert})
    else:
        form = ProductForm()
        return render(request, 'add_product.html', {'form': form})