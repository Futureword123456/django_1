from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import TemplateView


def temp_show(request):
    """模板引擎"""
    return render_to_response('detail.html')


def temp_filter(request):
    list_city = ['长沙', '北京', '武汉']
    price = 1000000000
    return render(request, 'temp_filter.html',{
        'list_city':list_city,
        'price':price
    })


class ShowClassView(TemplateView):
    """class视图"""
    template_name = 'show_class.html'
