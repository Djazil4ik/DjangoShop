from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
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

class SignUpPage(FormView):
    template_name = 'shopapp/signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUpPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(SignUpPage, self).get(*args, **kwargs)

def logout_view(request):
    logout(request)
    # Redirect to desired page after logout (e.g., login page)
    return redirect('login')

def profile(request):
    return render(request, 'profile.html')