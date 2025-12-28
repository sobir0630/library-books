from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, viewsets, filters
from django_filters import rest_framework as django_filters

from .models import Author, Product, Category, Order
from .serializers import AuthorSerializer, ProductSerializer, CatigorySerializer
from .filters import ProductFilter


# Create your views here.
class AuthorCreatedSerializer(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CustomPagination(PageNumberPagination):
    page_size = 3
    
class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    pagination_class = CustomPagination
    
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ProductFilter
    search_fields = ['name', 'author__name', 'disc']

class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CatigorySerializer


class ListViewSet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
