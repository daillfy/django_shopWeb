from django.contrib import admin
from django.urls import path, include

from order import views

app_name='order'

urlpatterns = [
    path(r'create/', views.order_create, name='order_create'),
]


