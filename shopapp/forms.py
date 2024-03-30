from django.forms import forms, ModelForm, ImageField, Textarea, TextInput
from .models import Seller, Product


class SellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = ('username', 'about', 'avatar')

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'slug', 'description', 'price', 'img')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the post'}),
            'slug': TextInput(attrs={'class': 'form-control', 'placeholder': 'Copy the title with no space and a hyphen in between'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Description of the Product'}),
            'price': TextInput(attrs={'class': 'form-control', 'placeholder': 'Price in $'}),
        }