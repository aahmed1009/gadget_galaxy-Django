from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
# Create your views here.
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
def category_new(request):
    return HttpResponse("New Category Page")

def category_update(request, id):
    return HttpResponse(f"Update Category Page for ID {id}")

