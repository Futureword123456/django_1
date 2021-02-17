# -*- coding: utf-8 -*-
# @Time : 2021/2/16 0016
# @Author : yang
# @Email : 2635681517@qq.com
# @File : urls.py
from django.conf.urls import url

from oauth import views
app_name = 'oauth'
urlpatterns = [
    # url(r'^index/$', views.index, name='index'),
    url(r'^temp/show/$',views.temp_show,name='temp_show'),
    url(r'^temp/filter/mine$', views.temp_filter, name='temp_filter'),
    url(r'^show/class/$',views.ShowClassView.as_view(),name='show_class'),
]
