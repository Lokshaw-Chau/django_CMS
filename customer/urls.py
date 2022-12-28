from . import views
from django.conf.urls import url
from django.urls import path
from .views import login, register, logout, information, show_info


app_name = 'customer'
urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('logout/', logout),
    path('showinfo/', show_info, name='show_info'),
    path('info/', information, name='info'),
]