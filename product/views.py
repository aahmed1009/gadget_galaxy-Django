from django.shortcuts import render, get_object_or_404 
from product.models import Product
from category.models import Category
from .models import Product
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

# Simple test views for adding and updating
def product_new(request):
    return HttpResponse("<h1>New Product Page</h1>")

def product_update(request, id):
    return HttpResponse(f"<h1>Update Product Page for ID {id}</h1>")

