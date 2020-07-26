"""crud_products URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_products import views
from app_products.views import ProductsAppView 

products_app_view = ProductsAppView()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products_app_view.index, name='index'),
    path('index.html', products_app_view.index, name='index'),
    path('create.html', products_app_view.create, name='create'),
    path('productEdit/<int:id>/',products_app_view.productEdit, name='productEdit'),
    path('productDelete/<int:id>/',products_app_view.productDelete, name='productDelete'),
    path('api/', include('app_products.urls')),
]
#  path('deleteevaluator/<int:id>/', views.deleteevaluator, name='deleteevaluator'),