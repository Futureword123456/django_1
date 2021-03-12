# -*- coding: utf-8 -*-
# @Time : 2021/3/10 0010
# @Author : yang
# @Email : 2635681517@qq.com
# @File : forms.py
import re

import form as form
from django import forms

"""导入forms"""


class LoginForm(forms.Form):
    """表单类"""
    SEX_CHOICES = (
        (1, '男'),
        (2, '女')
    )
    PATH = './/'
    re = '/^[0-9]*$'
    username = forms.CharField(label='用户名', max_length=64, required=False, initial="你好")
    email = forms.EmailField(label='电子邮箱')
    sex = forms.ChoiceField(label='性别', choices=SEX_CHOICES)
    birth = forms.DateField(label='生日')
    field = forms.FileField(label='文件上传')
    fieldpath = forms.FilePathField(label='文件路径', path=PATH)
    image = forms.ImageField(label='图片')
    Regex = forms.RegexField(label='正则', regex=re)
    remark = forms.CharField(label='备注', max_length=200, widget=forms.Textarea)
    # age = forms.IntegerField(label='年龄')
    age = forms.CharField(label='年龄', widget=forms.NumberInput)
    # password = forms.PasswordInput(label='密码')
    password = forms.CharField(label='密码', widget=forms.PasswordInput)


class UserLoginForm(forms.Form):
    """"用户登录"""
    username = forms.CharField(label='用户名', max_length=64)
    password = forms.CharField(label='密码', max_length=64, widget=forms.PasswordInput)
    verify_code = forms.CharField(label='验证码', max_length=6)

    def clean_username(self):
        """验证用户名"""
        username = self.cleaned_data['username']
        print(username)
        # 判断用户名是否为手机号码
        pattern = r'^(13[0-9]|14[5|7]|15[0|1|2|3|4|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$'
        if not re.search(pattern,username):
            raise forms.ValidationError('请输入正确的手机号码')


class UserRegistForm(forms.Form):
    """用户注册表单"""
    username = forms.CharField(label='用户名', max_length=64)
    nickname = forms.CharField(label='昵称', max_length=64)
    password = forms.CharField(label='密码', max_length=64, widget=forms.PasswordInput)
    repassword = forms.CharField(label='重复密码', max_length=64, widget=forms.PasswordInput)

    verify_code = forms.CharField(label='验证码', max_length=6)
