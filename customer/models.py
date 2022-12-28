# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    id = models.AutoField(primary_key=True, verbose_name= '地址编号')
    customer = models.ForeignKey('Customer', models.CASCADE, verbose_name= '消费者编号')
    location = models.TextField(blank=True, null=True, verbose_name= '地址信息')

    class Meta:
        db_table = 'address'


class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=10, verbose_name= '用户编号')
    status = models.IntegerField(choices=[(1, '已登录'),(0, '未登录')], verbose_name= '用户状态')
    password = models.CharField(max_length=20, blank=True, null=True, verbose_name= '密码')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name= '创建时间')
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name= '用户姓名')
    phone_number = models.CharField(max_length=13, blank=True, null=True, verbose_name= '用户电话')

    class Meta:
        db_table = 'customer'
