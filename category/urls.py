from django.urls import path
from .views import *

urlpatterns = [
    path('', category_list, name='category_list'),  
]