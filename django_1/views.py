# -*- coding: utf-8 -*-
# @Time : 2021/2/13 0013
# @Author : yang
# @Email : 2635681517@qq.com
# @File : views.py
import os
from datetime import datetime


from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse
from django.shortcuts import render, render_to_response, redirect
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


def index_one(request):
    """访问重定向到 index_two"""
    # url = reverse('index_two')
    # return HttpResponseRedirect(url)
    return redirect(index_two)
    # return HttpResponse("index one")


def index_two(request):
    return HttpResponse("index two")


"""请求对象"""


def print_request(request):
    print(request)
    """得到ip"""
    ip = request.META['REMOTE_ADDR']
    print(ip)
    """用户的浏览器信息"""
    user_agent = request.META['HTTP_USER_AGENT']
    print(user_agent)

    return HttpResponse()


"""响应对象"""


def print_resp(request):
    # 使用render
    now = datetime.now()
    html = render_to_response('index.html', {
        'now': now
    })
    return HttpResponse(html, content_type='text/plain')


def print_json(request):
    user_info = {
        'username': "杨华钟",
        'age': 22
    }
    # import json
    # user_info = json.dumps(user_info)
    # return HttpResponse(user_info,content_type='application/json')
    return JsonResponse(user_info)


"""打印响应对象"""


def attr(request):
    resp = HttpResponse("打印响应对象", status=404)
    """重写设置http的状态码"""
    # resp.status_code=204
    """打印http状态码"""
    resp.write('2020')
    # print(resp.status_code)
    return resp


# 可以实现导出excel
def print_image(request):
    try:
        file_name = os.path.join(BASE_DIR, 'static\\长江大学期末考试安排.xlsx')
        response = FileResponse(open(file_name, 'rb'))
    except Exception as e:
        print(e)
    return HttpResponse(response, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


def print_filter(request):
    """模板过滤器的使用"""
    list_word = [
        'view',
        'model',
    ]
    now = datetime.now()
    user_info={
        'username':"李四",
        'age':None,
        'sex': False
    }
    import math
    pi=math.pi
    html = '<h1>主标题</h1><script >alert("55555")</script>'
    str1 = "<h1>我是主标题</h1>"
    return render(request, 'filter.html', {
        'list_word': list_word,
        'now':now,
        'user_info':user_info,
        'pi':pi,
        'str1':str1,
        'html':html
    })


""""获取url中的参数"""
from django.views.generic.base import TemplateView

"""渲染图片、文字"""


def temp_image(request):
    img_url = '/medias/images/background.jpg'
    user_info = {
        'username': '杨华钟',
        'age': 22
    }

    list_city = ['长沙', '北京', '武汉']
    list_prod = [
        {'name': "名称1", 'price': 100, },
        {'name': "名称2", 'price': 200, },
        {'name': "名称3", 'price': 300, },
        {'name': "名称4", 'price': 400, },
    ]
    bool = True
    return render(request, 'car.html', {
        'img_url': img_url,
        'user_info': user_info,
        'list_city': list_city,
        'list_prod': list_prod,
        'bool': bool

    })


def temp_tag(request):
    """模板标签的使用"""
    list_city = ['长沙', '北京', '武汉']
    list_prod = [
        {'name': "名称1", 'price': 100, },
        {'name': "名称2", 'price': 200, },
        {'name': "名称3", 'price': 300, },
        {'name': "名称4", 'price': 400, },
    ]
    user_info = {
        'username': '杨华钟',
        'age': 22
    }
    list_order = []
    return render(request, 'tag.html', {
        'list_city': list_city,
        'list_prod': list_prod,
        'list_order': list_order,
        'user_info': user_info
    })


def article(request, year):
    # print('year:{0}'.format(year))
    # 用get获取月份前端url传过来参数
    month = request.GET.get('month', None)
    # 产生500
    # raise ValueError
    raise PermissionDenied
    # print('month:{0}'.format(month))
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


def page_500(request):
    """重写500响应页面"""
    return render_to_response('500.html')


def page_404(request, exception):
    """重写404响应页面"""
    return render(request, '404.html')
