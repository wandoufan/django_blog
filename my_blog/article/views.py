from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .forms import ArticlePostForm
# 引入login装饰器
from django.contrib.auth.decorators import login_required
import sys
sys.path.append('../')
from user.models import UserInfo


@login_required
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
            # 保存数据，但暂时不提交到数据库中
            article_temp = atricle_post_form.save(commit=False)
            # 从UserInfo表中获取user对象作为Article表中的作者
            article_temp.author = UserInfo.objects.get(username=request.user.username)
            # print('UserInfo表中的用户：', UserInfo.objects.all())
            # print('当前登录用户：', request.user.username)
            # 将文章数据保存到数据库
            article_temp.save()
            info = '文章已保存成功'
            article_list = Article.objects.filter(id=article_temp.id)
            return render(request, 'article/show.html', {'article_list': article_list, 'info': info})
            # return HttpResponse('数据已保存成功！')
        else:
            # 报错并返回错误原因
            return HttpResponse('报错：%s' % atricle_post_form.errors)
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
        article_list = Article.objects.filter(title=query_title)
        if len(article_list) == 0:
            return HttpResponse('没有查到标题为 %s 的文章' % query_title)
        else:
            info = '查询标题为 %s 的文章' % query_title
            return render(request, 'article/show.html', {'article_list': article_list, 'info': info})
    else:
        return render(request, 'article/query.html')


@login_required
def article_delete(request):
    """
    删除博客文章
    """
    if request.method == 'POST':
        delete_id = request.POST.get('id', 0)
        article_list = Article.objects.filter(id=delete_id)
        if len(article_list) == 0:
            return HttpResponse('没有查到id为 %s 的文章' % str(delete_id))
        else:
            article = article_list[0]
            # print('文章作者：', article.author.username)
            # print('当前登录账户：', request.user.username)
            # 仅当文章创建者和当前登录账户一致时才有权限删除文章
            if article.author.username == request.user.username:                
                article.delete()
                return HttpResponse('标题为 %s 的文章删除成功' % article.title)
            else:
                return HttpResponse('当前登录账户为%s, 无权限删除%s创建的文章' %(request.user.username, article.author.username))
    else:
        return render(request, 'article/delete.html')


@login_required
def article_update(request):
    """
    修改博客文章
    """
    if request.method == 'POST':
        update_id = request.POST.get('id', 0)
        update_title = request.POST.get('title', 0)
        update_body = request.POST.get('body', 0)
        article_list = Article.objects.filter(id=update_id)
        if len(article_list) == 0:
            return HttpResponse('没有查到id为 %s 的文章' % str(update_id))
        else:
            article = article_list[0]
            # print('文章作者：', article.author.username)
            # print('当前登录账户：', request.user.username)
            # 仅当文章创建者和当前登录账户一致时才有权限删除文章
            if article.author.username == request.user.username: 
                # 当页面输入新的标题或文章内容时博客随之更新，当页面没有填写新内容时标题或文章内容保持不变
                article.title = update_title if update_title != '' else article.title
                article.body = update_body if update_body != '' else article.body
                article.save()
                info = '修改了id为 %s 的文章，新内容如下：' % str(update_id)
                return render(request, 'article/show.html', {'article_list': article_list, 'info': info})
            else:
                return HttpResponse('当前登录账户为%s, 无权限修改%s创建的文章' %(request.user.username, article.author.username))
    else:
        return render(request, 'article/update.html')


def article_list(request):
    """
    显示所有的博客文章
    """
    article_list = Article.objects.all()
    if len(article_list) == 0:
        return HttpResponse('当前没有用户创建任何文章')
    else:
        info = '所有博客文章如下所示：'
        return render(request, 'article/list.html', {'article_list': article_list, 'info': info})