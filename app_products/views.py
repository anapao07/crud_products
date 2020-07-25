from django.shortcuts import render
from rest_framework import viewsets
from .models import Products
from .serializers import ProductsSerializer

def index(request):
    return render(request,'app_products/index.html')



class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()