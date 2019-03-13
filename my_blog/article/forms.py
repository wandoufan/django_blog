# 引入表单类
from django import forms
# 引入文章模型
from .models import Article


# 文章的表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = Article
        # 指明从html表单中返回的字段
        # fields = '__all__'
        fields = ('title', 'body')
        