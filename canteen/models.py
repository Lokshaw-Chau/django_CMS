# This is an auto-generated Django model module.

# You'll have to do the following manually to clean this up:

#   * Rearrange models' order

#   * Make sure each model has one field with primary_key=True

#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior

#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table

# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

class Canteen(models.Model):

    id = models.AutoField(primary_key=True, verbose_name= '餐厅编号')

    name = models.CharField(max_length=50, blank=True, null=True, verbose_name= '餐厅名称')

    location = models.TextField(blank=True, null=True, verbose_name= '餐厅位置')

    number_of_wicket = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True, verbose_name= '餐厅窗口数')

    status = models.IntegerField(choices=[(1, '营业中'),(0, '休息中')], verbose_name='餐厅状态')

    class Meta:

        db_table = 'canteen'


class Administrator(models.Model):

    id = models.CharField(primary_key=True, max_length =20, verbose_name= '管理员编号')

    status = models.IntegerField(choices=[(1, '可使用'),(0, '已注销')], verbose_name= '管理员状态')

    password = models.CharField(max_length=20, blank=True, null=True , verbose_name= '密码')

    creat_time = models.DateTimeField(auto_now_add= True, verbose_name= '创建时间')

    name = models.CharField(max_length=50, blank=True, null=True , verbose_name= '管理员姓名')

    manage = models.ManyToManyField(Canteen)

    class Meta:

        db_table = 'administrator'