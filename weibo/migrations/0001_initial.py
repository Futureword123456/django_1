# Generated by Django 2.2.7 on 2021-02-19 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500, verbose_name='内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('source', models.CharField(blank=True, max_length=10, null=True, verbose_name='信息来源')),
            ],
            options={
                'db_table': 'weibo',
            },
        ),
        migrations.CreateModel(
            name='WeiboUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('nickname', models.CharField(max_length=64, verbose_name='昵称')),
            ],
            options={
                'db_table': 'weibo_user',
            },
        ),
        migrations.CreateModel(
            name='WeiboImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='weibo', verbose_name='图片')),
                ('weibo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weibo.Weibo')),
            ],
            options={
                'db_table': 'weibo_images',
            },
        ),
        migrations.AddField(
            model_name='weibo',
            name='user',
            field=models.ForeignKey(on_delete='用户', to='weibo.WeiboUser'),
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='关注时间')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_from', to='weibo.WeiboUser', verbose_name='关注人')),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_to', to='weibo.WeiboUser', verbose_name='被关注人')),
            ],
            options={
                'db_table': 'weibo_friends',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=256, verbose_name='评论内容')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='评论使劲按')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weibo.WeiboUser', verbose_name='评论的用户')),
                ('weibo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weibo.Weibo', verbose_name='关联的微博')),
            ],
            options={
                'db_table': 'weibo_comments',
            },
        ),
    ]
