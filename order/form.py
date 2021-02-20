#用户注册和登录时的验证
from django import forms
from .models import Order

# 用户提交订单的流程
#1.提供一个表单个用户填写
#2.根据用户填写的内容生成一个新的order实例，然后将购物车中的商品放到OrderItem中，并于Order实例建立外键关系
#3.清理全部购物车内容，然后重定向到用户的一个操作成功界面
class OrderCreate(forms.ModelForm):
    class Meta:
        model=Order
        fields=['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
