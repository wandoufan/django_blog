# 引入表单类
from django import forms
# 引入 User 模型
from django.contrib.auth.models import User
from .models import UserInfo


# 用户登录表单，继承forms.Form类
class UserLoginForm(forms.Form):
    class Meta:
        # 指明数据模型来源
        model = UserInfo
        # 指明从html表单中返回的字段
        # fields = '__all__'
        fields = ('username', 'password')


# 用户注册表单，继承类
class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')