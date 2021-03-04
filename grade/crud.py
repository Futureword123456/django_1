# -*- coding: utf-8 -*-
# @Time : 2021/3/4 0004
# @Author : yang
# @Email : 2635681517@qq.com
# @File : crud.py


"""新增数据"""
from grade.models import Grade, Student
# for i in range(0,11):
#     user_obj = Student(student_name='杨华钟{}'.format(i))
#     user_obj.save()
user_list = Student.objects.get(student_name='杨华钟2')
user = Grade(student=user_list,subject_name='数据结构',score=120,year=2020)
user.save()

