from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .forms import ArticlePostForm


def article_create(request):
    """
    创建博客文章
    """
    # 如果用户提交了数据，就将数据保存，之后给用户反馈结果
    if request.method == 'POST':
        # 将提交的数据赋值到表单实例中
        atricle_post_form = ArticlePostForm(request.POST)
        # 判断提交数据是否合法
        if atricle_post_form.is_valid():
            atricle_post_form.save()
            return HttpResponse('数据已保存成功！')
        else:
            # 报错并返回错误原因
            return HttpResponse(atricle_post_form.errors)
    # 如果第一次匹配到url，用户还没有填写内容时，跳转到创建博客页面
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
        query_title = request.POST.get('title', 0)
        article_list = Article.objects.filter(title = query_title)
        # 按标题查询可能会查出多篇文章，目前暂时先只返回第一篇文章
        article = article_list[0]
        info_dict = {'title':article.title, 'body':article.body, 'created':article.created}
        return render(request, 'article/show.html', info_dict)
    else:
        return render(request, 'article/query.html')


