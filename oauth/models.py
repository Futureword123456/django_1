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
        db_table = 'user'
        ordering = ['-updated_at']


"""学生详细信息"""


class UserDetail(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE)

    sign = models.CharField('用户签名', max_length=256)
    isonline = models.IntegerField('是否在线', choices=(
        ('1', '是'),
        ('2', '否'),
        ('3', '离开'),
        ('4', '忙碌'),
        ('5', '隐身'),
    ), default='1')
    birthday = models.DateTimeField('生日')
    bloodtype = models.IntegerField('血型', choices=(
        ('1', 'A'),
        ('2', 'B'),
        ('3', 'O'),
        ('4', 'AB'),
        ('5', '其他')
    ), default='1')
    professional = models.TextField('职业', max_length=256)

    class Meta:
        db_table = 'user_detail'


class UserAddress(CommonUtils):
    """用户地址"""
    user = models.ForeignKey(Student, verbose_name='学生',on_delete=models.CASCADE)
    phone = models.CharField('收件人电话', max_length=11)
    address = models.CharField('收件人地址', max_length=64)
    zip_code = models.CharField('邮编', max_length=10, null=True, blank=True)
    is_vaild = models.BooleanField('是否有效', default=True)

    class Meta:
        db_table = 'user_address'


# Create your models here.


class ProxyStudent(Student):
    class Meta:
        proxy = True

    def get_name(self):
        """获取学生姓"""
        return self.name[0]
