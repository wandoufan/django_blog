# 引入表单类
from django import forms
# 引入文章模型
from .models import Article


# 文章的表单类
class ArticlePostForm(forms.Form):
    class Meta:
        # 指明数据模型来源
        model = Article
        # fields = ('title', 'author', 'body', 'created')
        fields = ('title', 'body', 'created')