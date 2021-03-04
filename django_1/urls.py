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
from django.views.static import serve

from django_1 import views, settings

handler500 = 'django_1.views.page_500'
handler404 = 'django_1.views.page_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/$', views.index),
    # 重定向
    # 学生成绩
    url(r'^grade/', include('grade.urls', namespace='grade')),
    url(r'^index/one/$', views.index_one, name='index_one'),
    url(r'^index/two2$', views.index_two, name='index_two'),
    # 打印请求对象
    url(r'^print/request/$',views.print_request,name='print_request'),
    # 响应对象实验
    url(r'^print/resp/$',views.print_resp,name='print_resp'),
    # 响应json对象"""
    url(r'^print/json/$',views.print_json,name='print_json'),
    # 打印响应对象
    url(r'^print/resp/attr/$',views.attr,name='print_attr'),
    url(r'^time/$', views.now_time),
    # 打印图片
    url(r'^print/image/$',views.print_image,name='print_image'),
    # 模板过滤器的使用
    url(r'^print/filter/$',views.print_filter,name='print_filter'),

    # 模板引擎选择
    # url(r'^temp/show/',views.temp_show,name='temp_show'),
    url(r'^temp/image/',views.temp_image,name='temp_image'),
    # 模板标签的使用
    url(r'^temp/tag/', views.temp_tag, name='temp_tag'),


    url(r'^article/(?P<year>[0-9]{4})/$', views.article, name='article_detail'),

    # url(r'^auth/', include('auth.urls',namespace='auth')),
    # path('auth/', include('auth.urls')),
    # 把其他模块的url引进来
    url(r'^auth/', include('oauth.urls', namespace='auth')),
    # 从html加载
    url(r'^now/$', views.now_use_file),
    # 微博模块
    url(r'^weibo/', include('weibo.urls', namespace='weibo')),
]
"""添加自定义的静态资源"""
urlpatterns += [url(r'^medias/(?P<path>.*)$', serve, {
    'document_root': settings.MEDIAS_ROOT,

}),]
