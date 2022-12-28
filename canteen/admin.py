from django.contrib import admin

# Register your models here.
from .models import Canteen, Administrator

admin.site.register(Canteen)
admin.site.register(Administrator)