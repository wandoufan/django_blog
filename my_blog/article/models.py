from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# from taggit.managers import TaggableManager
from PIL import Image


class Article(models.Model):
    """
    定义博客中文章的属性
    """
    # 文章标题
    title = models.CharField(max_length=150)
    # 文章作者
    # author = models.CharField(max_length=50)
    # 文章正文
    body = models.TextField()
    # 文章创建时间
    # 参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
