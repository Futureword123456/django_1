# Generated by Django 2.2.7 on 2021-02-18 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0009_auto_20210218_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('phone', models.CharField(max_length=11, verbose_name='收件人电话')),
                ('address', models.CharField(max_length=64, verbose_name='收件人地址')),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='邮编')),
                ('is_vaild', models.BooleanField(default=True, verbose_name='是否有效')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oauth.Student', verbose_name='学生')),
            ],
            options={
                'db_table': 'user_address',
            },
        ),
    ]
