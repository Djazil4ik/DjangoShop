from django import forms
from .models import Seller, Product


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ('name', 'about', 'avatar')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'slug', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the blog'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Copy the title with no space and a hyphen in between'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content of the Blog'}),
        }