from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category
# Create your views here.
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    return HttpResponse(f"<h1>Category Detail Page for {category.name}</h1>")
def category_new(request):
    return HttpResponse("New Category Page")

def category_update(request, id):
    return HttpResponse(f"Update Category Page for ID {id}")


