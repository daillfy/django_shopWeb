from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from app1.models import Product
from cart.cart import Cart
from cart.forms import CartAddProduct


@require_POST  #使该视图仅接受post请求
def cart_add(request, product_id):
    cart=Cart(request)
    product=get_object_or_404(Product, id=product_id)
    form =CartAddProduct(request.POST)
    if form.is_valid():
        cd=form.cleaned_data
        cart.add(product=product,quality=cd['quality'], update_quality=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart=Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def total_price(request):
    cart = Cart(request)
    cart.total_price()
    return redirect('cart:cart_detail')


def clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form']=CartAddProduct(initial={'quality':item['quality'],'update':True})
    return render(request,'cart_detail.html', locals())
