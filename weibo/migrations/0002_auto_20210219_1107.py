# Generated by Django 2.2.7 on 2021-02-19 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weibo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='评论时间'),
        ),
    ]
