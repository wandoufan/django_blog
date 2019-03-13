from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .forms import ArticlePostForm


def article_create(request):
    """
    创建博客文章
    """
    # 判断用户是否提交了数据
    if request.method == 'POST':
        # 将提交的数据赋值到表单实例中
        atricle_post_form = ArticlePostForm(request.POST)
        # 判断提交数据是否合法
        if atricle_post_form.is_valid():
            atricle_post_form.save()
            return HttpResponse('数据已保存成功！')
        else:
            # 报错并返回错误原因
            return HttpResponse('表单内容有误，请重新填写！', atricle_post_form.errors)
    # 如果用户请求获取数据
    else:
        atricle_post_form = ArticlePostForm()
        content = {'atricle_post_form': atricle_post_form}
        return render(request, 'article/create.html', content)


def article_query(request):
    """
    查询博客文章
    """
    # 判断用户是否提交了数据
    if request.method == 'POST':
        query_title = request.POST.get['title']
        return HttpResponse('查询内容：', query_title)
    else:
        return HttpResponse('没有使用POST方法')


