from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from app1 import views

app_name='app1'


from django.urls import path
urlpatterns = [
    path('', views.product_list, name='all'),
    path('<slug:category_slug>/', views.product_list, name='this_category_list'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]