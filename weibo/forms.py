# -*- coding: utf-8 -*-
# @Time : 2021/3/10 0010
# @Author : yang
# @Email : 2635681517@qq.com
# @File : forms.py
import re

import form as form
from django import forms

from weibo.models import WeiboUser

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
    """"用户登录创建表单"""
    """前台传到的后台数据"""
    username = forms.CharField(label='用户名', max_length=64)
    password = forms.CharField(label='密码', max_length=64, widget=forms.PasswordInput)
    verify_code = forms.CharField(label='验证码', max_length=6)

    def clean_username(self):
        """验证用户名,前端验证,每一个字段的验证"""
        """得到前端传的数据"""
        username = self.cleaned_data['username']
        print(username)
        # 判断用户名是否为手机号码
        pattern = r'^(13[0-9]|14[5|7]|15[0|1|2|3|4|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$'
        if not username:
            raise forms.ValidationError('请输入用户名')
        if not re.search(pattern, username):
            raise forms.ValidationError('请输入正确的手机号码')
        return username

    def clean_password(self):
        """验证密码"""
        password = self.cleaned_data['password']
        if len(password) < 6 or len(password) > 12:
            raise forms.ValidationError('请输入6到12位的密码')
        if not password:
            raise forms.ValidationError('请输入密码')

    def clean(self):
        """多个字段进行组合验证 后端验证"""
        cleaned_data = super().clean()
        print(cleaned_data)
        # username = cleaned_data['username']
        """取用户名和密码"""
        username = cleaned_data.get('username', None)
        password = cleaned_data.get('password', None)

        if username and password:
            # """数据库查询用户名和密码"""
            user_list = WeiboUser.objects.filter(username=username)
            if user_list.count() == 0:
                raise forms.ValidationError('用户名不匹配')
            if not user_list.filter(password=password).exists():
                raise forms.ValidationError('密码错误，请重新输入')
        return cleaned_data


class UserRegistForm(forms.Form):
    """用户注册表单"""
    username = forms.CharField(label='用户名', max_length=64)
    nickname = forms.CharField(label='昵称', max_length=64)
    password = forms.CharField(label='密码', max_length=64, widget=forms.PasswordInput)
    repassword = forms.CharField(label='重复密码', max_length=64, widget=forms.PasswordInput)
    verify_code = forms.CharField(label='验证码', max_length=6)


class UserForm(forms.ModelForm):
    """从模型创建表单"""

    class Meta:
        model = WeiboUser
        """需要显示的字段"""
        fields = ['username', 'password', 'nickname']
        """密码显示......界面显示修改"""
        """css的class"""
        widgets = {
            'password': forms.PasswordInput(attrs={
                'class': 'text-err'
            })
        }
        labels = {
            'username': '手机号码'
        }
        """重写错误"""
        error_messages = {
            'username': {
                'required': '请输入手机号码',
                'max_length': '最长不超过32位'
            }
        }
