#上下文管理器

from .cart import Cart

#上下文管理器，接受一个request请求对象，返回一个要添加到request上下文字典的python对象

def cart(request):
    return {'cart':Cart(request)}

#需要在setting中加上我们的自定义上下文管理器
