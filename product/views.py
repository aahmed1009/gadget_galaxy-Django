from django.shortcuts import render, get_object_or_404 ,redirect
from product.models import Product
from category.models import Category
from .models import Product
from django.http import HttpResponse
from category.models import Category
from .forms import ProductForm
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
# TODO:class Method
# def product_new(request):
#     categories = Category.objects.all()
#     context = {'categories': categories}

#     if request.method == 'POST':
#         Product.create_from_request(request.POST, request.FILES)
#         context['msg'] = 'Product added successfully'

#     return render(request, 'new_product.html', context)
def product_new(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_admin')
    else:
        form = ProductForm()
    
    return render(request, 'new_product.html', {'form': form})
def product_update(request, id):
    product = get_object_or_404(Product, pk=id)
    categories = Category.objects.all()
    
    if request.method == 'POST':
        data = {
            'name': request.POST['name'],
            'description': request.POST['description'],
            'price': request.POST['price'],
            'stock': request.POST['stock'],
            'sku': request.POST['sku'],
            'category_id': request.POST['category'],
            'image': request.FILES.get('image')  
        }
        Product.update_product(id, data)
        return redirect('product_admin')

    return render(request, 'update_product.html', {'product': product, 'categories': categories})


def soft_delete_product(request, id):
    Product.soft_delete(id)
    return redirect('product_list')

def hard_delete_product(request, id):
    Product.hard_delete(id)
    return redirect('product_list')
def product_admin(request):
    products = Product.get_all()
    return render(request, 'product_admin.html', {'products': products})

def product_soft_delete(request, id):
    Product.soft_delete(id)
    return redirect('product_admin')

def product_hard_delete(request, id):
    Product.hard_delete(id)
    return redirect('product_admin')
