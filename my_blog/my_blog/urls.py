"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from article import views as article_views
from user import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('article-create/', article_views.article_create, name='article_create'),
    path('article-query/', article_views.article_query, name='article_query'),
    path('article-delete/', article_views.article_delete, name='article_delete'),
    path('article-update/', article_views.article_update, name='article_update'),
    path('article-list/', article_views.article_list, name='article_list'),
    path('user-login/', user_views.user_login, name='user_login'),
    path('user-create/', user_views.user_create, name='user_create'),
]
