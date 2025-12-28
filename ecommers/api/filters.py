from django_filters import rest_framework as django_filters  # pip install django-filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    
    class Mete:
        model = Product
        fields = ['catigory', 'min_price', 'max_price']