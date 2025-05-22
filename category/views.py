# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from .models import Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category
# Create your views here.
# def category_list(request):
#     categories = Category.objects.all()
#     return render(request, 'category_list.html', {'categories': categories})
# def category_detail(request, id):
#     category = get_object_or_404(Category, id=id)
#     return HttpResponse(f"<h1>Category Detail Page for {category.name}</h1>")
# def category_new(request):
#     return HttpResponse("New Category Page")

# def category_update(request, id):
#     return HttpResponse(f"Update Category Page for ID {id}")



class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

