from django.db.models import Sum, Max, Min, Avg
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from grade.models import Grade, Student


def page_stas(request):
    """ 聚合及统计 """
    """计算杨华钟的成绩总和"""
    grade_list = Grade.objects.filter(student__student_name='杨华钟').aggregate(total=Sum('score'))
    print(grade_list['total'])

    # 求数据结构成绩的最高分
    grade_max = Grade.objects.filter(subject_name='数据结构').aggregate(high_score=Max('score'))
    print(grade_max['high_score'])

    # 求数据结构成绩的最低分i
    grade_min = Grade.objects.filter(subject_name='数据结构').aggregate(min_score=Min('score'))
    print(grade_min['min_score'])

    # 查询数据结构的平均分
    avg_grade = Grade.objects.filter(subject_name='数据结构').aggregate(avg=Avg('score'))
    print("平均分是:{0}".format(avg_grade['avg']))
    # 统计每个学生成绩的总和1
    # select student_name,Sum(score) from Grade group by student_name
    total_list = Grade.objects.values_list('student__student_name').annotate(Sum('score'))
    for i in total_list:
        print('学生成绩总和是{0}'.format(i))

    # 统计每个学生成绩的总和2
    user_list = Student.objects.all().annotate(total_score=Sum('stu_grade__score'))
    for i in user_list:
        if i.total_score is None:
            continue
        else:
            print(i.student_name, i.total_score)

    user_zhang = Student.objects.get(pk=1)
    for item in user_zhang.stu_grade.all():
        print(item.subject_name, item.score)
    return HttpResponse('ok')
