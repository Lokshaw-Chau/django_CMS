from django.shortcuts import render,get_object_or_404,redirect
from canteen.models import Canteen
from dish.models import Dish,CustomerOrder
from .models import Wicket,Merchant
from wicket.forms import LoginForm
from django.contrib import messages
# Create your views here.

def show_wicket(request):
    template_name = 'canteen/shop_list.html'
    context = {
        'canteen_with_wicket_list': Canteen.objects.all(),
        'wicket_list': Wicket.objects.all()
    }
    print(Wicket.objects.all())
    return render(request, template_name, context)

def login(request):
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            id = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            # identy 表示
            print("[DEBUG][POST][LOGIN][username]:{}".format(id))
            print("[DEBUG][POST][LOGIN][password]:{}".format(password))
            try:
                print("[DEBUG][POST][STATE]:查询商户数据库")
                user_cus = Merchant.objects.get(id=id)
                if user_cus.password == password:
                    print("[DEBUG][POST][USERNAME]:{}".format(user_cus.id))
                    print("[DEBUG][POST][STATE]:登录成功")
                    messages.success(request, '{}登录成功！'.format(user_cus.id))
                    user_cus.status = 1
                    user_cus.save()
                    request.session['is_login'] = True
                    print(user_cus.id)
                    request.session['merchant_id'] = user_cus.id
                    request.session['merchant_name'] = user_cus.name
                    return redirect('/wicket/index/')
                else:
                    print("[DEBUG][POST][STATE]:密码不正确")
                    message = "密码不正确"
            except:
                print("[DEBUG][POST][STATE]:商户不存在")
                message = "商户不存在"
    return render(request, 'wicket/login.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        return render(request, 'wicket/shop_list.html', locals())
    user_id = request.session['merchant_id']
    print("[DEBUG][REQUEST][退出]]")
    print("[DEBUG][REQUEST][USER_ID]:{}".format(user_id))
    try:
        user = Merchant.objects.get(id=user_id)
        print("[DEBUG][REQUEST][退出]]：退出商户身份")
        user.status = 0 
        user.save()
    except:
        print("[DEBUG][request][STATE]:退出错误，无法更新数据库中用户状态")

    request.session.flush()
    return render(request, 'customer/index.html', locals())

def show_owns(request):
    template_name = 'wicket/dish_list.html'
    merchant_id = request.session['merchant_id']
    merchant = Merchant.objects.filter(id = merchant_id).first()
    wickets = merchant.wickets.all().first()
    # TODO:筛选order
    dishes = Dish.objects.filter(wic = wickets)
    orderlist = []
    for i in dishes:
        orderlist.extend(CustomerOrder.objects.filter(dis_id = i))
        
    context = {
        'order_list': orderlist
    }
    return render(request, template_name, context)

def change_status(request, order_id):
    order = get_object_or_404(CustomerOrder, id=order_id)
    print('test')
    if order.status == 0:
        order.status = 1
    else:
        order.status = 0
    order.save()
    messages.success(request, '状态改变成功')
    return redirect("/wicket/index/")