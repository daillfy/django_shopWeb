from django.contrib import admin
from django.urls import path, include

from cart import views

app_name='cart'
urlpatterns = [
    path(r'', views.cart_detail, name='cart_detail'),
    path(r'add/<int:product_id>/', views.cart_add, name='cart_add'),
    path(r'remove/<int:product_id>/', views.cart_remove, name='cart_remove')
    #当有参数时，一般用path
]


