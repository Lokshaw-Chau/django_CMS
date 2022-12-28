# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from canteen.models import Canteen 
from django.urls import reverse


class Wicket(models.Model):
    id = models.AutoField(primary_key=True, verbose_name= '窗口编号')
    can_id = models.ForeignKey(Canteen, models.CASCADE , verbose_name= '餐厅编号')
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name= '窗口名称')
    status = models.IntegerField(choices=[(1, '营业中'),(0, '未营业')], verbose_name= '窗口状态')

    class Meta:
        db_table = 'wicket'

    def change_status_url(self):
        return reverse("wicket:change_status", kwargs={'wicket_id': self.id})


class Merchant(models.Model):
    id = models.CharField(primary_key=True, max_length=20, verbose_name= '商户编号')
    status = models.IntegerField(choices=[(1, '可使用'),(0, '已注销')], verbose_name= '商户状态')
    password = models.CharField(max_length=20, blank=True, null=True, verbose_name= '商户密码')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name= '创建时间')
    name = models.CharField(max_length=20, blank=True, null=True, verbose_name= '商户昵称')
    wickets = models.ManyToManyField(to = Wicket)

    class Meta:
        db_table = 'merchant'

    