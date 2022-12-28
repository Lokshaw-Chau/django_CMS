from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.core.paginator import Paginator
from django.http import JsonResponse
from .forms import LoginForm, RegisterForm, AddressForm
from django.contrib import messages

from .models import Customer, Address


def register(request):
    register_form = RegisterForm()
    if request.session.get('is_login', None):  
        return render(request, 'customer/index.html', locals()) 
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid(): 
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            tel = register_form.cleaned_data['tel']
            name = register_form.cleaned_data['name']

            if password1 != password2: 
                print("两次输入的密码不同！")
                message = "两次输入的密码不同！"
                return render(request, 'customer/register.html', locals())
            else:
                same_id_cus = Customer.objects.filter(name=username)
                if same_id_cus: 
                    message = '顾客用户名已经存在~请换一个'
                    return render(request, 'customer/register.html', locals())
                else:
                    new_cus = Customer.objects.create(customer_id=username, phone_number=tel,
                                                      password=password1,status = 1,name=name)
                    new_cus.save()
                    login_form = LoginForm()
                    message = "注册成功！"
                    return render(request, 'customer/login.html', locals())  # 自动跳转到登录页面
    else:
        return render(request, 'customer/register.html', locals())

    return render(request, 'customer/register.html', locals())


def login(request):
    login_form = LoginForm()
    if request.session.get('is_login', None):
        print("已经登陆")
        return render(request, 'customer/index.html', locals())

    if request.method == "POST":
        login_form = LoginForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            customer_id = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            print("[DEBUG][POST][LOGIN][username]:{}".format(customer_id))
            print("[DEBUG][POST][LOGIN][password]:{}".format(password))
            try:
                print("[DEBUG][POST][STATE]:查询顾客用户数据库")
                user_cus = Customer.objects.get(customer_id=customer_id)
                if user_cus.password == password:
                    print("[DEBUG][POST][USERNAME]:{}".format(user_cus.customer_id))
                    print("[DEBUG][POST][STATE]:登录成功")
                    messages.success(request, '{}登录成功！'.format(user_cus.customer_id))
                    user_cus.status = 1
                    user_cus.save()
                    request.session['is_login'] = True
                    request.session['user_id'] = user_cus.customer_id
                    request.session['user_name'] = user_cus.name
                    request.session['tel'] = user_cus.phone_number
                    return render(request, 'customer/index.html', locals())
                else:
                    print("[DEBUG][POST][STATE]:密码不正确")
                    message = "密码不正确"
            except:
                print("[DEBUG][POST][STATE]:用户不存在")
                message = "用户不存在"
    return render(request, 'customer/login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return render(request, 'customer/index.html', locals())
    user_id = request.session['user_id']
    print("[DEBUG][REQUEST][退出]]")
    print("[DEBUG][REQUEST][USER_ID]:{}".format(user_id))
    try:
        user = Customer.objects.get(customer_id=user_id)
        print("退出顾客身份")
        user.status = 0 
        user.save()
    except:
        print("退出错误，无法更新数据库中用户状态")

    request.session.flush()
    return render(request, 'customer/index.html', locals())


def information(request):
    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/customer/login/')

    address_form = AddressForm()
    user_id = request.session['user_id']
    customer = Customer.objects.filter(customer_id=user_id).first()

    if request.method == "POST":
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            new_location = address_form.cleaned_data['location']
            try:
                cus_info = Address.objects.create(customer=customer,location=new_location)
                cus_info.customer = customer
                cus_info.save()
                request.session['location'] = new_location
                messages.success(request, '个人地址添加成功！')
                return redirect('/customer/showinfo')
            except:
                messages.warning(request, '个人地址添加失败')
                return render(request, 'customer/information.html', locals())

    return render(request, 'customer/information.html', locals())


def show_info(request):
    customer_id = request.session['user_id']
    customer = Customer.objects.filter(customer_id = customer_id).first()
    context = {
        'address_list':Address.objects.filter(customer=customer)
    }
    return render(request, 'customer/show_info.html',context)
