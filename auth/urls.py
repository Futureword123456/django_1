# -*- coding: utf-8 -*-
# @Time : 2021/2/13 0013
# @Author : yang
# @Email : 2635681517@qq.com
# @File : urls.py
from django.conf.urls import url
from django.urls import path

from auth import views

app_name = 'auth'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
]
