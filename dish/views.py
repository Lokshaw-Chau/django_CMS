from django.shortcuts import render
from wicket.models import Wicket
from .models import Dish, CustomerOrder
from customer.models import Customer
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.


def show_dish(request):
    template_name = 'dish/dish_list.html'
    context = {
        'wicket_with_dish_list': Wicket.objects.all(),
        'dish_list': Dish.objects.all(),
    }

    return render(request, template_name, context)


def show_order(request):
    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/customer/login/')

    template_name = 'dish/my_order.html'

    user_id = request.session['user_id']

    context = {
        'order_list': CustomerOrder.objects.filter(customer_id=user_id),
    }
    return render(request, template_name, context)


def get_order(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    user_id = request.session['user_id']

    try:
        user = Customer.objects.filter(customer_id=user_id).first()
        order = CustomerOrder.objects.create(dis_id=dish, customer_id=user)
        order.status = 0
        order.amount = order.dis_id.price
        print(order.amount)
        order.contact_number = order.customer_id.phone_number
        order.save()
        messages.success(request, '下单成功，订单号为 (Order ID-{}). 请支付 {} 元'.format(order.id, order.dis_id.price))
        return redirect("/dish")

    except ObjectDoesNotExist:
        messages.warning(request, "你还没有订单哦~")
        return redirect("dish:show_order")