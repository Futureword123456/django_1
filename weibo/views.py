from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def Page_User(request,page):
    """对用户进行分页处理"""
    return HttpResponse('ok')
