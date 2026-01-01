from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import StandardResultsSetPagination
from main.models import Product, Category, Order, OrdemItem
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    OrderSerializer,
    OrdemItemSerializer
)
from .filters import ProductFilter, OrderFilter, OrdemItemFilter, CategoryFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProductSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return ProductSerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAdminUser()]
        return super().get_permissions()
    

class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CategorySerializer
        elif self.action in ["create", "update", "partial_update"]:
            return CategorySerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAdminUser()]
        return super().get_permissions()
    

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return OrderSerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAuthenticated()]
        return super().get_permissions()
    

class OrdemItemViewSet(ModelViewSet):
    queryset = OrdemItem.objects.all()
    serializer_class = OrdemItemSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrdemItemFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrdemItemSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return OrdemItemSerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAuthenticated()]
        return super().get_permissions()