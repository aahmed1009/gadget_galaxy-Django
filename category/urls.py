from django.urls import path
from .views import *

urlpatterns = [
    # path('', category_list, name='category_list'),
    #   path('<int:id>/', category_detail, name='category_detail'),
    # path('new/', category_new, name='category_new'),
    # path('update/<int:id>/', category_update, name='category_update'),
     path('', CategoryListView.as_view(), name='category_list'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('new/', CategoryCreateView.as_view(), name='category_create'),
    path('<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]