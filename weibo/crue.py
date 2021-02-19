# -*- coding: utf-8 -*-
# @Time : 2021/2/19 0019
# @Author : yang
# @Email : 2635681517@qq.com
# @File : crue.py

from weibo.models import WeiboUser as User

user_obj = User(username='杨华钟', password='123456', nickname='无限可能')
user_obj.save()

user_obj1 = User.objects.create(username='admin', password='password',nickname='未来世界')
