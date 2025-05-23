"""
URL configuration for gadget_galaxy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# from category.views import category_list
from product.views import product_list, product_detail, index
from django.conf import settings
from django.conf.urls.static import static
from user.views import register, activate
from django.contrib.auth import views as auth_views
from user.views import register, activate, login_view
from django.contrib.auth.views import LogoutView
urlpatterns = [
#     path('admin/', admin.site.urls),
    path('', include('product.urls')),     
# path('categories/', include('category.urls')),
  path('', index, name='index'),
  path('admin/', admin.site.urls),
    
 path('register/', register, name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('login/', login_view, name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('categories/', include('category.urls')),
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
