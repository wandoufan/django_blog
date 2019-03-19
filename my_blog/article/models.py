from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import sys
sys.path.append('../')
from user.models import UserInfo
# from django.urls import reverse
# from taggit.managers import TaggableManager
# from PIL import Image


class Article(models.Model):
    """
    定义博客中文章的属性
    """
    # 文章标题
    title = models.CharField(max_length=150)
    # 文章作者
    # 通过外键与UserInfo模型关联
    author = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    # 文章正文
    body = models.TextField()
    # 文章创建时间
    # 参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)
    # 文章更新时间
    # 参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        # 使显示信息为文章标题，而非一个'Article object'
        return self.title
