from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'), 
    path('products/', product_list, name='product_list'),  
    path('products/<int:product_id>/', product_detail, name='product_detail'),  
]
