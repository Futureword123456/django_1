# -*- coding: utf-8 -*-
# @Time : 2021/3/4 0004
# @Author : yang
# @Email : 2635681517@qq.com
# @File : urls.py

from django.conf.urls import url

from grade import views

urlpatterns = [
    # 聚合及统计
    url(r'^stas/$', views.page_stas, name='page_stas'),
]