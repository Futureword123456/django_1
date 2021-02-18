# Generated by Django 2.2.7 on 2021-02-18 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='学生姓名')),
                ('sex', models.CharField(choices=[('1', '男'), ('2', '女'), ('9', '不详')], default='1', max_length=2, verbose_name='性别')),
                ('age', models.PositiveIntegerField(default=0, verbose_name='年龄')),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='登录名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('phone', models.IntegerField(verbose_name='电话号码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
        ),
    ]
