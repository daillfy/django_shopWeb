#创建应该cart类，来对购物车进行处理

from decimal import Decimal

from django.conf import settings
from app1.models import Product


class Cart:
    def __init__(self, request):
        """
        初始化购物车
        :param request:
        """
        self.session=request.session
        cart=self.session.get(settings.CART_SESSION_ID)  #判断公路网是否存在
        if not cart:
            #如果不存在就创建一个
            cart=request.session[settings.CART_SESSION_ID]={}
        self.cart=cart

    def add(self, product, quality=1, update_quality=False):
        """
        添加商品
        :return:
        """
        product_id=str(product.id)  #为什么要变成字符串类型，因为json的键是字符类型的，所以必须变成字符串类型
        if product_id not in self.cart:
            self.cart[product_id]={'quality':0,'price':str(product.price)}
        if update_quality:
            self.cart[product_id]['quality']=quality
        else:
            self.cart[product_id]['quality']+=quality
        self.save()  #session的保存

    def save(self):
        #设置session.modified为true，中间件在看到这个属性的时候就会保存session
        self.session.modified=True

    def remove(self, product):
        """
        删除商品
        :return:
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()  #每次进行修改更新都需要保存

    def __iter__(self):
        """
        遍历展示购物车的商品,因为要从数据库中读取，所以为了提高效率采用迭代器的方法
        :return:
        """
        product_ids=self.cart.keys()
        #获取所有佛如购物车对象
        products=Product.objects.filter(id__in=product_ids)
        cart=self.cart.copy()
        for product in products:
            cart[str(product.id)]['product']=product  #cart里面存的是session，session的键都是字符串

        for item in cart.values():
            item['price']=Decimal(item['price'])  #Decimal将字符串类型变成浮点型
            item['total_price']=item['price']*item['quality']
            yield item

    def __len__(self):
        """
        显示一共有多少商品
        :return:
        """
        return sum(item['quality'] for item in self.cart.values())

    def total_price(self):
        """
        求总的价格
        :return:
        """
        return sum(Decimal(item['price']*item['quality'])for item in self.cart.values())


    def clear(self):
        """
        清空购物车
        :return:
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()

