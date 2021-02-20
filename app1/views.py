from django.shortcuts import render, get_object_or_404

from app1.models import Product, Category
from cart.forms import CartAddProduct


def product_list(request, category_slug=None):#category_slug选定的特定种类
    category=None  #如果不指定类别就是查询所有的商品信息，如果指定类别category_slug不是None就是查询当前的
    categories=Category.objects.all()  #所有的类别
    products=Product.objects.filter(available=True)  #available只有可选的才能展示
    if category_slug:  #根据类别展示对应的商品
        category=get_object_or_404(categories, slug=category_slug)  #当前商品对应的类别
        #get_object_or_404导入对应的库，如果找不到会自动报告错误
        products=products.filter(category=category)
        #找到所有对应类别的商品
    return render(request,'all.html',locals())


def product_detail(request, id ,slug):
    product=get_object_or_404(Product,id=id,slug=slug)
    cart_product_form=CartAddProduct()  #将商品添加到购物车里面
    return render(request,'detail.html', locals())

