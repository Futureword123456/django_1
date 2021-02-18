from django.db import models


# Create your models here.
class Student(models.Model):
    """学生表"""

    name = models.CharField(max_length=64, verbose_name='学生姓名')
    sex = models.CharField('性别', max_length=2, choices=(
        ('1', '男'),
        ('2', '女'),
        ('9', '不详')
    ), default='1')
    age = models.PositiveIntegerField('年龄', default=0)
    username = models.CharField('登录名', max_length=64, unique=True)
    password = models.CharField('密码', max_length=256)
    phone = models.IntegerField('电话号码', max_length=11)
    email = models.EmailField('邮箱')
    create_at = models.DateTimeField('创建时间',auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间',auto_now=True)
