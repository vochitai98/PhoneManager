"""webdienthoai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views


    # path('', views.home),


    # path('register',views.RegisterPage,name='register'),
    # path('',views.LoginPage,name='login'),
    # path('home/',views.HomePage,name='home'),
    # # path('logout/',views.LogoutPage,name='logout'),
  
    # path('listProduct', listProduct, name='listProduct'),
urlpatterns = [
    path('',views.home,name="home"),
    # path('',views.home,name="home"),
    path('cart',views.view_cart,name="cart"),
    path('search',views.getDTbysearch,name="search"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('getdtbyhang',views.get_DTByHang,name="getdtbyhang"),
    path('getdtbygia',views.get_DTbyGia,name="getdtbygia"),
    path('detail',views.detail,name="detail"),
    path('search',views.getDTbysearch,name="search"),
    path('add/<int:dt_id>/', views.add_cart, name='add_cart'),
    path('addhome/<int:dt_id>/', views.add_cart_home, name='add_cart_home'),

    path('remove/<int:dt_id>/', views.remove_product, name='remove_product'),
    path('cart/increase_quantity/<int:product_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease_quantity/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
]
