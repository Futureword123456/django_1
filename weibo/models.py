from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserManager(models.Manager):
    def top_users(self):
        # 2、调用现有的方法
        return self.all().order_by('-create_at'[:5])


class WeiboUser(models.Model):
    """ 微博用户 """
    USER_STATUS = (
        (2, '限制用户'),
        (1, '正常'),
        (0, '删除'),
    )
    username = models.CharField('用户名', max_length=64)
    password = models.CharField('密码', max_length=256)
    nickname = models.CharField('昵称', max_length=64)
    status = models.SmallIntegerField('用户状态', choices=USER_STATUS, default=1)
    create_at = models.DateTimeField('创建时间', null=True, blank=True)
    updated_at = models.DateTimeField('最后修改时间', null=True, blank=True)
    content = models.CharField('内容', max_length=256)
    """自定义管理器"""
    users = UserManager()

    class Meta:
        db_table = "weibo_user"
        ordering = ['id']

    def __str__(self):
        return 'User;{},pk:{},status:{},nickname:{}'.format(self.username, self.pk, self.status, self.nickname)


"""添加代理
"""


# class MyUser(WeiboUser):
#     """扩充功能"""
#
#     class Meta:
#         proxy = True
#
#     def get_format_username(self):
#         return self.username[:3] + '*****'
#

class Weibo(models.Model):
    """微博"""
    content = models.CharField('内容', max_length=500)
    user = models.ForeignKey(WeiboUser, '用户')
    created_at = models.DateTimeField('发布时间', auto_now_add=True)
    source = models.CharField('信息来源', max_length=10, null=True, blank=True)

    class Meta:
        db_table = 'weibo'


class WeiboImage(models.Model):
    """微博图片"""
    weibo = models.ForeignKey(Weibo, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='weibo', verbose_name='图片')

    class Meta:
        db_table = 'weibo_images'


class Comment(models.Model):
    """微博的评论"""
    content = models.CharField('评论内容', max_length=256)
    create_at = models.DateTimeField('评论时间', auto_now_add=True)
    user = models.ForeignKey(WeiboUser, verbose_name='评论的用户', on_delete=models.CASCADE)
    weibo = models.ForeignKey(Weibo, verbose_name='关联的微博', on_delete=models.CASCADE)

    class Meta:
        db_table = 'weibo_comments'


class Friend(models.Model):
    """好友关系"""
    user_from = models.ForeignKey(WeiboUser, verbose_name='关注人', related_name='user_from', on_delete=models.CASCADE)
    user_to = models.ForeignKey(WeiboUser, verbose_name='被关注人', related_name='user_to', on_delete=models.CASCADE)
    created_at = models.DateTimeField('关注时间', auto_now_add=True)

    class Meta:
        db_table = 'weibo_friends'
