# -*- coding: utf-8 -*-
# @Time : 2021/3/10 0010
# @Author : yang
# @Email : 2635681517@qq.com
# @File : forms.py
import form as form
from django import forms


class LoginForm(forms.Form):
    """表单类"""
    username = forms.CharField(label='用户名', max_length=64)
