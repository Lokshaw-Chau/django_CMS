from django.contrib import admin

# Register your models here.
from .models import Dish, CustomerOrder

admin.site.register(Dish)
admin.site.register(CustomerOrder)