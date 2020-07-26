from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Products
from .serializers import ProductsSerializer
from .forms import ProductsForm


def index(request):
    return render(request, 'app_products/index.html')


def create(request):
    form = ProductsForm()
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'app_products/create.html', context)


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
