from django.shortcuts import render, render_to_response


# Create your views here.
from django.views.generic import TemplateView


def temp_show(request):
    """模板引擎"""
    return render_to_response('detail.html')


class ShowClassView(TemplateView):
    """class视图"""
    template_name = 'show_class.html'
