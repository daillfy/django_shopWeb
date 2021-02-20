from django.shortcuts import render
from cart.cart import Cart
from order.form import OrderCreate
from .models import OrderItem

def order_create(request):
    cart=Cart(request)
    if request.method=='POST':
        form=OrderCreate(request.POST)
        if form.is_valid():
            order=form.save()  #创建一个订单对象，并且保存
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'], price=item['price'],quality=item['quality'])
                #生成order书籍信息
            #成功生成OrderItem后清除购物车
            cart.clear()
            return render(request,'created.html', locals())

    else:
        form=OrderCreate()
    return render(request,'create.html',locals())
