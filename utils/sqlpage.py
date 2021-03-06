# -*- coding: utf-8 -*-
# @Time : 2021/3/6 0006
# @Author : yang
# @Email : 2635681517@qq.com
# @File : sqlpage.py


"""分页类"""
from django.db import connection


class SqlPaginator(object):
    def __init__(self, sql, params, page_size):
        super(SqlPaginator, self).__init__()
        self.sql = sql
        self.params = params
        self.page_size = page_size

    def page(self, now_page):
        offset = (now_page - 1) * self.page_size
        sql = self.sql + ' limit %s offset %s'
        print(sql)
        cursor = connection.cursor()
        # 3、根据游标执行sql
        self.params.extend([self.page_size, offset])
        rest = cursor.execute(sql, self.params)
        # 4、获取查询结果
        rows = cursor.fetchall()
        return rows

