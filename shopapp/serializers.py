from rest_framework import serializers
from .models import Seller, Product

class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.HyperlinkedIdentityField(read_only=True, view_name='seller-detail')
    class Meta:
        model = Product
        fields = '__all__'
        
class SellerSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True)
    class Meta:
        model = Seller
        fields = '__all__'