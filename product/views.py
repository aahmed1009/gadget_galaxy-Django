from django.shortcuts import render, get_object_or_404 
from product.models import Product
from category.models import Category
from .models import Product
from django.http import HttpResponse
from category.models import Category
# Create your views here.
def index(request):
    return render(request, 'index.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})



# def product_new(request):
#     categories = Category.objects.all()
#     context = {'categories': categories}

#     if request.method == 'POST':
#         pname = request.POST['pname']
#         description = request.POST['description']
#         price = request.POST['price']
#         stock = request.POST['stock']
#         sku = request.POST['sku']
#         category_id = request.POST['category']
#         image = request.FILES['image']


#         Product.objects.create(
#             name=pname,
#             description=description,
#             price=price,
#             stock=stock,
#             sku=sku,
#             image=image,
#             category_id=category_id
#         )
#         context['msg'] = 'Product added successfully'

#     return render(request, 'new_product.html', context)
def product_new(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    if request.method == 'POST':
        Product.create_from_request(request.POST, request.FILES)
        context['msg'] = 'Product added successfully'

    return render(request, 'new_product.html', context)
def product_update(request, id):
    return HttpResponse(f"<h1>Update Product Page for ID {id}</h1>")
def product_delete(request, id):
    return HttpResponse(f"<h1>delete Product Page for ID {id}</h1>")
