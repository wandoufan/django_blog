from django.contrib import admin
from .models import UserInfo


# 注册UserInfo到admin中
admin.site.register(UserInfo)