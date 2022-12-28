from django.contrib import admin

# Register your models here.
from .models import Wicket, Merchant

admin.site.register(Merchant)
admin.site.register(Wicket)