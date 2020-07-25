from django.shortcuts import render
from rest_framework import viewsets
from .models import Products
from .serializers import ProductsSerializer



class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()