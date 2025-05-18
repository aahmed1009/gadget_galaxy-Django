from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'), 
    path('products/', product_list, name='product_list'),  
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('products/new/', product_new, name='product_new'), 
    path('products/update/<int:id>/', product_update, name='product_update'),
    path('products/delete/<int:id>/', product_delete, name='product_delete'),  
]