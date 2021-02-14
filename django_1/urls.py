"""django_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls import url

from django_1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/$', views.index),
    url(r'^time/$', views.now_time),

    url(r'^article/(?P<year>[0-9]{4})/$', views.article, name='article_detail'),

    # url(r'^auth/', include('auth.urls',namespace='auth')),
    # path('auth/', include('auth.urls')),
    # 把其他模块的url引进来
    re_path(r'^auth/', include('auth.urls', namespace='auth')),
    # 从html加载
    url(r'^now/$', views.now_use_file),
]
