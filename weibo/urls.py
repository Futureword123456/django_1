# -*- coding: utf-8 -*-
# @Time : 2021/2/20 0020
# @Author : yang
# @Email : 2635681517@qq.com
# @File : urls.py

from django.conf.urls import url

from weibo import views

app_name = 'weibo'
urlpatterns = [
    # 对用户数据进行分页
    url(r'^user/(?P<page>\S+)/$', views.Page_User, name='Page_User'),
    # orm查询练习
    url(r'^search/$', views.page_sarch, name='page_sarch'),
    # 事务练习
    url(r'^trans/$', views.trans, name='trans'),
    #
    url(r'^trans_with/$', views.trans_with, name='trans_with'),
    # 手动控制事务
    url(r'^trans_hand/$', views.trans_hand, name='trans_hand'),
    # q函数的使用
    url(r'^q/$', views.page_q, name='trans_hand'),

]
