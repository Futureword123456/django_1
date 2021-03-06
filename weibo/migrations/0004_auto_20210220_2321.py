# Generated by Django 2.2.7 on 2021-02-20 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weibo', '0003_auto_20210220_2309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weibo',
            options={},
        ),
        migrations.AlterModelOptions(
            name='weibouser',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='weibouser',
            name='status',
            field=models.SmallIntegerField(choices=[(2, '限制用户'), (1, '正常'), (0, '删除')], default=1, verbose_name='用户状态'),
        ),
    ]
