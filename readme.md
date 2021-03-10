null、blank是否为空值、null
db_column  数据库中对应的字段名称
default 不填写该字段时的默认值
primary_key、unique 主键、唯一索引
verbose_name 供编程查看的字段名称（易于阅读）
help_text 帮助文字
choices 可供选择的选择，如:性别的选项（男，女）
get_FOO_display() 展示choices对应的值
CharField（max_length、）EmailField、TextField 字符串、文本
DateField、DatetimeField 时间日期
FileField、ImageField  文本、图片
IntegerField、SmallIntegerField 整数
FloatField、DecimalField 小数
auto_now 更新时间为记录更改的时间
auto_now_add记录创建时间



模型的元数据
使用Mata类来表示
    class Meta:
        """修改数据库的名称"""
        db_table = 'students'
        ordering = ['-updated_at']
        
 外键关联
 
 
 django的增删改查
 1、使用模型的save()保存数据
 user_obj = User(username = 'admin',password = 'password)
 user_obj.save()
 2、使用模型的create()新增加的数据
 user_obj = User.objects.create(username='admin',password = 'password')
 user_obj.pk
3、使用get()查询单条数据
User.objects.get(pk=1)
user_obj.id
使用模型的all()查询所有的数据
User.objects.all()
user_obj

使用save()修改数据
使用update()批量修改数据
user_obj = User.objects.all().update(*args,**kwargs)

使用delete()删除数据
删除单条数据
user_obj = User.objects.get(pk=1)
user_obj.delete()
删除多条记录
User.objects.all().delete()


1.Paginator常用属性和方法：
（1）count:总共有多少条数据。
（2）num_pages:总共有多少页
（3）page_range:页面的区间。比如有三页，那么就是range(1,4)。
2.Page常用属性和方法：
（1）has_next:是否还有下一页。
（2）has_previous:是否还有上一页。
（3）next_page_number: 下一页的页码。
（4）previous_page_number:上一页的页码：
（5）number：当前页。
（6）start_index: 当前这一页的第一条数据的索引值。
（7）end_index:当前这一页的最后一条数据的索引值。

表单
action---表单提交的url地址
method---表单请求的方式
enctype---请求内容形式
textarea----多行文本
text------单行文本
password------密码
email----邮箱
url-----URL
number-----数字
color------颜色
日期时间等(date,month,week,time,datetime,datetime-local)

选择标签
单选
<input type ="radio">
多选
<input type ="checkbox">
下拉选择
<select><option></option></select>
文件上传
<input type="file">
隐藏表单域
<input type="hidden">
按钮
<input type="button">

在视图中获取表单的值：
GET请求
request.GET.get('name',None)
POST请求
request.POST.get('name',None)
