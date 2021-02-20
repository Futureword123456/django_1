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
"""批量修改数据"""
user_list = User.objects.all()
user_list.update(password='aa123')
