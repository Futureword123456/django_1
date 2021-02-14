# -*- coding: utf-8 -*-
# @Time : 2021/2/13 0013
# @Author : yang
# @Email : 2635681517@qq.com
# @File : views.py
import os
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import loader
from django.urls import reverse
from django.utils import encoding

from django_1.settings import BASE_DIR


def index(request):
    """重定向"""
    url = reverse('article_detail', args=(2020,))
    """不同模块之间的重定向"""
    url_auth = reverse('auth:index')
    print(url_auth)
    return HttpResponse("hello" + url)


""""获取url中的参数"""


def article(request, year):
    print('year:{0}'.format(year))
    # 用get获取月份前端url传过来参数
    month = request.GET.get('month', None)
    print('month:{0}'.format(month))
    return HttpResponse("article:" + year)


def now_time(request):
    """"显示系统当前时间"""
    now = datetime.now()
    html = """
        <html>
            <head>
                <style type = "text/css">
                    body{{color:red}}
                </style> 
            </head>
            <body>
                new:{0}
            </body>
        </html>
    """.format(now)
    return HttpResponse(html)


def now_use_file(request):
    """从html文件读取内容并返回"""
    html = ''
    now = datetime.now()
    # file_name = os.path.join(BASE_DIR, 'templates', 'index.html')
    # with open(file_name) as f:
    #     html = f.read()
    # html = html.replace("{0}", now.strftime('%Y-%M-%D'))
    # """使用loader.get_template直接上传到前端"""
    # print(html)
    # 使用django提供的方法
    # temp = loader.get_template('index.html')
    # html = temp.render({
    #
    # })
    # return HttpResponse(html)
    # 使用render
    # return render(request, 'index.html', {
    #     'now': now
    # })
    # 使用render_to_response()
    return render_to_response('index.html', {
        'now': now
    })
