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