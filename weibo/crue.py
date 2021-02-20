# -*- coding: utf-8 -*-
# @Time : 2021/2/19 0019
# @Author : yang
# @Email : 2635681517@qq.com
# @File : crue.py

from weibo.models import WeiboUser as User

"""新增数据"""
# user_obj = User(username='杨华钟', password='123456', nickname='无限可能')
# user_obj.save()
#
# user_obj1 = User.objects.create(username='admin', password='password',nickname='未来世界')
# """查询"""
# try:
#     user_obj = User.objects.get(pk=5)
# except Exception as e:
#     print('error')
#
# user_all = User.objects.all()
# for user in user_all:
#     print(user.username,end='|')
#
#
# user_obj = User.objects.get(pk=5)
# print(user_obj.nickname)
# user_obj.nickname = '世界'
# user_obj.save()
# """批量修改数据"""
# user_list = User.objects.all()
# user_list.update(password='aa123')

"""删除数据"""
# user_obj = User.objects.get(pk=7)
# user_obj.delete()
"""get_or_create有则返回，无则创建记录"""
# obj = User.objects.get_or_create(username='杨华钟',password='aa123',nickname='世界')
#
# obj1 = User.objects.get_or_create(username='杨',password='aa123',nickname='世界')
#
# user1 = User(username='user1',password=123,nickname='yan1')
# user2 = User(username='user2',password=123,nickname='yan2')
# user3 = User(username='user3',password=123,nickname='yan3')
# """插入多条数据"""
# User.objects.bulk_create([user1,user2,user3])
"""返回第一条/最后一条"""
# print(User.objects.first())
# print(User.objects.last())
"""返回数据库的记录数量"""
# print(User.objects.count())
"""结果集是否存在,存在则返回True,不存在则返回False"""
# print(User.objects.exists())
"""修改记录"""
user_obj = User.objects.get(pk=18)

user_obj.password = 'aaa'
user_obj.save()


