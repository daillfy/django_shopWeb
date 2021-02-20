from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    #商品的种类，一个种类对应多个商品
    name=models.CharField(max_length=200,db_index=True)
    #商品的简称，SlugField相当与一个网址，方便查询跳转,规范化URL
    slug=models.SlugField(max_length=200,db_index=True,unique=True)

    class Meta: #显示时候的描述
        ordering=('name',)  #通过name排序
        verbose_name='category'  #关键字显示
        verbose_name_plural='categories'

    def get_absolute_url(self):  #为了配置url的反向解析，通过类别具体到某一个商品
        return reverse('app1:this_category_list',args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category=models.ForeignKey(Category,related_name='categoy', on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    slug=models.SlugField(max_length=20)
    image=models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True) #商品是否可用
    created=models.DateTimeField(auto_now_add=True) #创建的时间，根据添加的时间自动添加
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        index_together=(('id','slug'))  #用id和slog创建联合索引

    def get_absolute_url(self):
        return reverse('app1:product_detail',args=[self.id, self.slug]) #shop是配置在主url里面的app路径名，product_detail是局部url中含有参数的url名

    def __str__(self):
        return self.name


