# Generated by Django 2.2.7 on 2021-02-18 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='id_no',
            field=models.CharField(default='', max_length=10, verbose_name='学号'),
            preserve_default=False,
        ),
    ]