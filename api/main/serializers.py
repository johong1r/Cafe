from rest_framework import serializers
from main.models import Product, Category, Order, OrdemItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'image', 'name', 'price', 'description', 'category']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class OrdemItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrdemItem
        fields = ['id', 'product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrdemItemSerializer(many=True, source='ordemitem_set')

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'status', 'items']


