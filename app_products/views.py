from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Products
from .serializers import ProductsSerializer
from .forms import ProductsForm


def index(request):
    queryset = Products.objects.all()
    context = {'ProdustList': queryset}
    return render(request, 'app_products/index.html',context)


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

def productEdit(request,id):
    queryset = Products.objects.get(id=id)
    if request.method == 'GET':
        form = ProductsForm(instance=queryset)
        context = {
            'form': form
        }
    else:
        form = ProductsForm(request.POST, instance= queryset)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'app_products/create.html', context)

def productDelete(request,id):
    queryset = Products.objects.get(id=id)
    queryset.delete()
    return redirect('index')

class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
