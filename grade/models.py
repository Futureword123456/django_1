from django.db import models


# Create your models here.
# 学生表
class Student(models.Model):
    student_name = models.CharField('学生姓名', max_length=32)

    class Meta:
        db_table = 'grade_students'


# 成绩表
class Grade(models.Model):
    """学生成绩"""

    student = models.ForeignKey(Student, null=True, related_name='stu_grade', on_delete=models.CASCADE)
    subject_name = models.CharField('科目', max_length=32)
    score = models.FloatField('分数', default=0)
    sort = models.IntegerField('排名',default=1)

    year = models.SmallIntegerField('年份')

    class Meta:
        db_table = 'grade'
