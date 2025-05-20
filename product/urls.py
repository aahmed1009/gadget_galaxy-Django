from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'), 
    # path('products/', product_list, name='product_list'),  
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('products/new/', product_new, name='product_new'), 
    path('products/update/<int:id>/', product_update, name='product_update'),
    # path('products/delete/<int:id>/', product_delete, name='product_delete'),
    # path('products/delete/<int:id>/', hard_delete_product, name='product_hard_delete'),
    # path('products/soft-delete/<int:id>/', soft_delete_product, name='product_soft_delete'),
    path('products/admin/', product_admin, name='product_admin'),
    # path('products/<int:id>/soft-delete/', product_soft_delete, name='product_soft_delete'),
    # path('products/<int:id>/hard-delete/', product_hard_delete, name='product_hard_delete'),
    path('products/<int:id>/update/', product_update, name='product_update'),
    #list using class based view
path('products/', ProductListView.as_view(), name='product_list'),
    #delete using class based view
path('products/<int:pk>/delete/', ProductSoftDeleteView.as_view(), name='product_delete'),


  
]