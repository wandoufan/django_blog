from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserInfo(AbstractUser):
    """
    声明用户信息
    继承django模型自带的User类，并添加自定义的属性方法
    """
    phone = models.CharField(max_length=20, blank=True, verbose_name='手机号码')

    def __str__(self):
        # username是来自于User类中的字段
        return self.username

