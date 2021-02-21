from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

from weibo.models import WeiboUser as User


# Create your views here.
def Page_User(request, page):
    print('==========')
    print(page)
    """对用户进行分页处理"""
    """每一页有1条数据"""
    page_size = 10
    """每页的数据结果集QuerySet"""
    user_list = User.objects.all()
    """分页器对象"""
    p = Paginator(user_list, page_size)
    print('总记录数:', p.count)
    print('总页数', p.num_pages)
    print('页码范围', p.page_range)
    try:
        """获取某一页的数据"""
        page_data = p.get_page(page)
        print('数据列表', page_data.object_list)
        print('是否还有下一页', page_data.has_next())
        print('是否还有上一页', page_data.has_previous())
        print('下一页的页码', page_data.next_page_number())
        print('上一页的页码', page_data.has_previous())
        print('当前页', page_data.number)
        print('当前这一页的第一条数据的索引', page_data.start_index())
        print('当前这一页的最后一条数据的索引值', page_data.end_index())
    except PageNotAnInteger as e:
        print('页码错误')
    except EmptyPage as e:
        print('没有数据了')

    return HttpResponse('ok')


def page_sarch(request):
    """查询条件练习"""
    # user10 = User.objects.filter(username='user10')
    # print(user10)
    # """区分大小写"""
    # user = User.objects.filter(nickname__contains='user10')
    # print(user)
    # """查询昵称姓ni的用户"""
    # ni = User.objects.filter(nickname__startswith='ni')
    # print(ni)
    """查询以小二结束的用户"""
    # user_list = User.objects.filter(nickname__endswith='长江大学')
    # print(user_list)
    # """用户多个状态的查询in"""
    # user_list = User.objects.filter(status__in=(4, 5))
    # print(user_list)
    # """查询用户状态大于四的结果"""
    # user_list = User.objects.filter(status__gt=4)
    # """查询用户状态大于等于四的结果"""
    # user_list = User.objects.filter(status__gte=4)
    # print(user_list)
    """查询空字符串"""
    try:
        user_list = User.objects.filter(remark__exact='')
        print(user_list.count())
    except Exception as e:
        print("字段不存在")
    return HttpResponse('ok')
