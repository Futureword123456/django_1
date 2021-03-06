# -*- coding: utf-8 -*-
# @Time : 2021/3/6 0006
# @Author : yang
# @Email : 2635681517@qq.com
# @File : sqlpage.py


"""分页类"""
import math

from django.db import connection


class PageNumError(Exception):
    pass


class SqlPaginator(object):
    def __init__(self, sql, params, page_size):
        super(SqlPaginator, self).__init__()
        self.sql = sql
        self.params = params
        self.page_size = page_size

    @property
    def page_count(self):
        """"""
        return math.ceil(self.count/self.page_size)

    @property
    def count(self):
        """ 数据库中总共有多少条记录 """
        # 查询数据总数的SQL
        count_sql = (
            'SELECT COUNT(1) FROM ('
            '{}'
            ') as count_record'
        ).format(self.sql)

        # print(self.sql)
        # print(self.params)
        try:
            # 2. 根据连接获取游标
            cursor = connection.cursor()
            # 3. 根据游标来执行SQL
            cursor.execute(count_sql, self.params)
            rest = cursor.fetchone()
            rest = rest[0]
        except:
            rest = 0
        return rest

    def page(self, now_page):
        """
        SELECT COUNT(1) FROM (
            SELECT `id`, `username`, `nickname` FROM `weibo_user`
            WHERE `id` > 20
        ) as count_record

        # 嵌套子查询
        获取当前页的数据
        :param now_page: 页码
        """
        # 判断页面是否超出了范围
        if now_page > self.page_count or now_page < 1:
            raise PageNumError
        offset = (now_page - 1) * self.page_size
        sql = self.sql + ' LIMIT %s OFFSET %s'
        print(sql)

        # 2. 根据连接获取游标
        cursor = connection.cursor()
        # 3. 根据游标来执行SQL
        sql_params = []
        for p in self.params:
            sql_params.append(p)
        sql_params.extend([self.page_size, offset])
        rest = cursor.execute(sql, sql_params)
        # 4. 获取查询结果
        rows = cursor.fetchall()
        return rows
