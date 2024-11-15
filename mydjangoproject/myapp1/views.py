from django.shortcuts import render
from .models import Client, Product, Sale

def index(request):
    clients = Client.objects.all()
    products = Product.objects.all()
    sales = Sale.objects.all()
    return render(request, 'index.html', {
        'clients': clients,
        'products': products,
        'sales': sales,
    })
