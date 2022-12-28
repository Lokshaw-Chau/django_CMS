from django.shortcuts import render
from .models import Canteen
# Create your views here.

def index(request):
    return render(request, 'base.html')

def show_canteen(request):
    template_name = 'canteen/canteen_list.html'
    context = {'canteen_list': Canteen.objects.filter(status=1)}
    return render(request, template_name, context)