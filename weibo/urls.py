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
    # sql使用
    url(r'^sql/$', views.page_sql, name='page_sql'),


    url(r'^pure/sql/$', views.page_pure_sql, name='page_pure_sql'),
    # 自定义分页器
    url(r'^page/paginator/sql/$', views.page_paginator_sql, name='page_paginator_sql'),
    url(r'^page/paginator/sql2/$', views.page_paginator_sql2, name='page_paginator_sql2'),
    # 表单的学习
    url(r'^form/page_form/first$', views.page_form_first, name='page_form_first'),
    # 以后登录
    url(r'^user/login$', views.user_login, name='user_login'),
    # 用户注册
    url(r'^user/regist$', views.user_regist, name='user_regist'),

]
