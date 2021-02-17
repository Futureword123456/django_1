# -*- coding: utf-8 -*-
# @Time : 2021/2/17 0017
# @Author : yang
# @Email : 2635681517@qq.com
# @File : oauth_extras.py
import locale
from decimal import Decimal

from asgiref import local
from django import template


register = template.Library()


def warning(value):
    """将第一个字符变红"""
    if value:
        return '<span class="text-red">' + value[0] + '</span>' + value[1:]
    return value


"""注册过滤器"""
register.filter('waring', warning)


def accounting(value, place=2):
    try:
        place = int(place)
    except:
        place = 2
    try:
        value = Decimal(value)
        locale.setlocale(locale.LC_ALL, '')
        return locale.format('%.*f', (place, value), 1)
    except Exception as e:
        return value


register.filter('accounting_format',accounting)