from django.contrib import admin

#将订单信息注册到后台管理
from .models import Order, OrderItem
# 我们让OrderItem类继承了admin.TabularInline类，然后在OrderAdmin类中使用了inlines参数指定OrderItemInline，
# 通过该设置，可以将一个模型显示在相关联的另外一个模型的编辑页面中。

class OrderItemOnline(admin.TabularInline):
    model=OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =  ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemOnline]

