from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo
from .forms import UserLoginForm
from .forms import UserCreateForm
from django.contrib.auth import authenticate, login, logout


def user_create(request):
    """
    创建新用户
    """
    if request.method == 'POST':
        user_create_form = UserCreateForm(request.POST)
        if user_create_form.is_valid():
            user = UserInfo.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            return HttpResponse('创建新用户成功')
        else:
            return HttpResponse('输入数据不合法：%s' % user_create_form.errors)
    else:
        return render(request, 'user/create.html')

def user_login(request):
    """
    用户登录
    """
    if request.method == 'POST':
        # 将提交的数据赋值到表单实例中
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            # cleaned_data方法得到一个包含表单数据的字典结构
            # info = user_login_form.cleaned_data
            # 检查账户密码是否有效，并得到一个user对象
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                # authenticate方法的返回值不为None说明账户有效，可以登录
                login(request, user)
                return HttpResponse('登录成功')
            else:
                return HttpResponse('账户或密码有误')
        else:
            return HttpResponse('输入数据不合法：%s' % user_login_form.errors)
    else:
        return render(request, 'user/login.html')

def user_logout(request):
    """
    用户注销
    """
    logout(request)
    return HttpResponse('注销成功')

