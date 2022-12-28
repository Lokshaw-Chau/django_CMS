from django.urls import path
from .views import index,show_canteen

app_name = 'canteen'
urlpatterns = [
    #path('', index),
    path('', show_canteen, name='canteen'),
]