from django_filters import FilterSet, CharFilter, NumberFilter
from main.models import Product, Category, Order, OrdemItem


class ProductFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')
    category = CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'min_price', 'max_price', 'category']


class CategoryFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name']


class OrderFilter(FilterSet):
    status = CharFilter(field_name='status', lookup_expr='iexact')
    user = CharFilter(field_name='user__full_name', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = ['status', 'user']


class OrdemItemFilter(FilterSet):
    product_name = CharFilter(field_name='product__name', lookup_expr='icontains')
    order_id = NumberFilter(field_name='order__id', lookup_expr='exact')

    class Meta:
        model = OrdemItem
        fields = ['product_name', 'order_id']