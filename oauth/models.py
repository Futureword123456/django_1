from django.db import models


class CommonUtils(models.Model):
    create_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)

    class Meta:
        """变成抽象类"""
        abstract = True


"""课程"""


class Course(CommonUtils):
    name = models.CharField('课程名称', max_length=64)

    class Meta:
        db_table = 'course'


# Create your models here.
class Student(CommonUtils):
    """学生表"""
    name = models.CharField(max_length=64, verbose_name='学生姓名')
    sex = models.CharField('性别', max_length=2, choices=(
        ('1', '男'),
        ('2', '女'),
        ('9', '不详')
    ), default='1')
    id_no = models.CharField('学号', max_length=10)
    age = models.PositiveIntegerField('年龄', default=0)
    username = models.CharField('登录名', max_length=64, unique=True)
    password = models.CharField('密码', max_length=256)
    phone = models.IntegerField('电话号码')
    email = models.EmailField('邮箱')
    """学生表和课程表是多对多的关系"""
    courses = models.ManyToManyField(Course)
    """内部类"""

    class Meta:
        """修改数据库的名称"""
        db_table = 'students'
        ordering = ['-updated_at']


class ProxyStudent(Student):
    class Meta:
        proxy = True

    def get_name(self):
        """获取学生姓"""
        return self.name[0]
