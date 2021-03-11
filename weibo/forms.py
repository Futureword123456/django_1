# -*- coding: utf-8 -*-
# @Time : 2021/3/10 0010
# @Author : yang
# @Email : 2635681517@qq.com
# @File : forms.py
import form as form
from django import forms

"""导入forms"""


class LoginForm(forms.Form):
    """表单类"""
    SEX_CHOICES = (
        (1, '男'),
        (2, '女')
    )
    username = forms.CharField(label='用户名', max_length=64, required=False, initial="你好")
    email = forms.EmailField(label='电子邮箱')
    sex = forms.ChoiceField(label='性别', choices=SEX_CHOICES)
    birth = forms.DateField(label='生日')
