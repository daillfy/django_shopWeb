from django.db import models
from app1.models import Product


class Order(models.Model):
    #创建顾客信息
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering=('-created',)

    def __str__(self):
        return f'Order {self.id}'

class OrderItem(models.Model):
    #创建订单信息
    #顾客与订单一对多关系，在多的一方关联
    #订单和商品，多对多关系，任意一方都可以关联
    order=models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='order_items', on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quality=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price*self.quality
