from django.urls import path
from .views import *

urlpatterns = [
    path('', category_list, name='category_list'),
    path('new/', category_new, name='category_new'),
    path('update/<int:id>/', category_update, name='category_update'),
]