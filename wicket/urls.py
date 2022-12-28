from django.urls import path
from .views import show_wicket, login, show_owns, logout,change_status

app_name = 'wicket'
urlpatterns = [
    #path('', index),
    path('wicket/', show_wicket, name='wicket'),
    path('wicket/login/', login),
    path('wicket/index/', show_owns),
    path('wicket/logout/', logout),
    path('change_status/<slug:order_id>', change_status, name='change_status'),
]