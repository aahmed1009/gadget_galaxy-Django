from django.shortcuts import render
from product.models import Product
from category.models import Category
from .models import Product
# Create your views here.



def index(request):
    return render(request, 'store/index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        product = None
    return render(request, 'store/product_detail.html', {'product': product})
