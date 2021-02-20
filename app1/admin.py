from django.contrib import admin

#将模型注册到管理后台
from .models import Category, Product

#创建管理员用户,登录后台管理
#python manage.py createsuperuser
#Username:用户名
#Email address
#Password

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']  #slug是一个规范化的url
    prepopulated_fields = {'slug':('name',)}  #让slug通过name自动生成

@admin.register(Product)
class ProducAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','available','created','updated']
    list_filter = ['available','created','updated']  #筛选字段
    list_editable = ['price','available']  #可编辑字段
    prepopulated_fields = {'slug':('name',)}