from datetime import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from weibo.models import WeiboUser as User, Comment, Weibo, WeiboUser


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
    # 是否为空值的查询 isnull
    # user_list = User.objects.filter(create_at__isnull=True)
    # print(user_list.count())
    """查询空字符串"""
    # try:
    #     user_list = User.objects.filter(remark__exact='')
    #     print(user_list.count())
    # except Exception as e:
    #     print("字段不存在")
    """查询是今天创建的用户"""
    date = datetime.now().date()
    print(date)
    user_list = User.objects.filter(create_at__date=date)
    print(user_list)
    """查询二月份创建的用户"""
    user_list = User.objects.filter(create_at__month='3')
    print(user_list)
    """查询记录"""
    comment_list = Comment.objects.filter(user__username__contains='user11')
    for item in comment_list:
        print(item.user.username)
    return HttpResponse('ok')


@transaction.atomic()
def trans(request):
    """事务练习
    用户发布新闻时顺便发布一条评论，不能失败
    """
    user = User.objects.get(pk=40605)
    """发布微博"""
    weibo = Weibo.objects.create(user=user, content='发布长江大学1')
    """发布评论"""
    comment = Comment.objects.create(user=user, content='微博评论', weibo=weibo)
    print('weibo', weibo.pk, 'comment:', comment.id)
    return HttpResponse('ok')


def trans_with(request):
    """事务练习
       用户发布新闻时顺便发布一条评论，不能失败
       """
    with transaction.atomic():
        user = User.objects.get(pk=40605)
        """发布微博"""
        weibo = Weibo.objects.create(user=user, content='发布长江大学11111')
        """发布评论"""
        comment = Comment.objects.create(user=user, content='微博评论222222', weibo=weibo)
        print('weibo', weibo.pk, 'comment:', comment.id)
    return HttpResponse("ok1")


def trans_hand(request):
    """手动控制事务"""
    user = User.objects.get(pk=40605)
    """发布微博"""
    try:
        """放弃自动提交"""
        transaction.set_autocommit(False)
        weibo = Weibo.objects.create(user=user, content='hand2')
        """发布评论"""
        comment = Comment.objects.create(user=user, content='微博评论2', weibo=weibo)
        transaction.commit()
        print('weibo', weibo.pk, 'comment:', comment.id)

    except:
        """不使用事务手动删除"""
        # weibo.delete()
        transaction.rollback()
    return HttpResponse('ok')


"""q函数的使用"""


def page_q(request):
    """查询username和nick0的信息"""
    # user_list = WeiboUser.objects.filter(username='user0')
    # user_list2 = WeiboUser.objects.filter(nickname='user0')
    # print(user_list)
    # print(user_list2)
    # or操作|
    # 从url中获得参数
    # name = request.GET.get('name',None)
    # query = Q(username=name) | Q(nickname=name)
    # user_list_q = WeiboUser.objects.filter(query)
    # for i in user_list_q:
    #     print('user:{0},status:{1},nickname:{2}'.format(i.username,i.status,i.nickname))
    # 从url中获取多个数据进行查询
    # username中获取数据
    username = request.GET.get('usernmae', None)
    query = Q()
    if username is not None:
        query = query & Q(username=username)
    # nickname获取数据
    nickname = request.GET.get('nickname', None)
    if nickname is not None:
        query = query & Q(nickname=nickname)
    user_list_q2 = WeiboUser.objects.filter(query)
    print(user_list_q2.count())
    print(user_list_q2)
    return HttpResponse('ok')
