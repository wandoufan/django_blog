# 引入表单类
from django import forms
from .models import UserInfo


# 用户的表单类
class UserInfoForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = UserInfo
        # 指明从html表单中返回的字段
        # fields = '__all__'
        fields = ('username', 'password')