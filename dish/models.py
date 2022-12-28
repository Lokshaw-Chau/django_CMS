# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from wicket.models import Wicket
from customer.models import Customer
from django.urls import reverse

class Dish(models.Model):
    id = models.AutoField(primary_key=True, verbose_name= '菜品编号')
    wic = models.ForeignKey(Wicket, models.CASCADE , verbose_name= '菜品窗口号')
    price = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True , verbose_name= '菜品价格')
    name = models.CharField(max_length=50, blank=True, null=True , verbose_name= '菜品名称')
    description = models.TextField(blank=True, null=True , verbose_name= '菜品描述')

    class Meta:
        db_table = 'dish'

    def get_order_url(self):
        return reverse("dish:get_order", kwargs={'dish_id': self.id})

class CustomerOrder(models.Model):
    id = models.AutoField(primary_key=True, verbose_name= '订单编号')
    customer_id = models.ForeignKey(Customer, models.CASCADE, verbose_name= '订单用户编号')
    dis_id = models.ForeignKey(Dish , models.CASCADE, verbose_name= '菜品编号')
    status = models.IntegerField(choices=[(0, '已下单'), (1, '已发货'), (2, '已收货'), (3, '已取消')], default=0, verbose_name='订单状态')
    amount = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True , verbose_name= '总价')
    creat_time = models.DateTimeField(blank=True, null=True , auto_now_add=True ,verbose_name= '创建时间')
    contact_number = models.CharField(max_length=13, blank=True, null=True , verbose_name= '联系方式')
    count = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True , verbose_name= '菜品数量')

    class Meta:
        db_table = 'customer_order'
    def change_status_url(self):
        print('test1')
        return reverse("wicket:change_status", kwargs={'order_id': self.id})