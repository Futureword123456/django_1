# Generated by Django 2.2.7 on 2021-02-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weibo', '0007_auto_20210221_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='weibouser',
            name='content',
            field=models.CharField(default=0, max_length=256, verbose_name='内容'),
            preserve_default=False,
        ),
    ]