from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .class_api import (
    ProductViewSet,
    CategoryViewSet,
    OrderViewSet,
    OrdemItemViewSet
)


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'order-items', OrdemItemViewSet, basename='ordemitem')


urlpatterns = [
    path('', include(router.urls)),
]