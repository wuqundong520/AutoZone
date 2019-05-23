# Generated by Django 2.1.1 on 2018-11-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_robotframework', '0009_auto_20181115_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_web_testcase',
            name='webfindmethod',
            field=models.CharField(max_length=200, verbose_name='方法|操作'),
        ),
        migrations.AlterField(
            model_name='add_web_testcase',
            name='webkwargesone',
            field=models.CharField(max_length=200, verbose_name='参数1'),
        ),
        migrations.AlterField(
            model_name='add_web_testcase',
            name='webkwargesthree',
            field=models.CharField(max_length=200, verbose_name='参数3'),
        ),
        migrations.AlterField(
            model_name='add_web_testcase',
            name='webkwargestwo',
            field=models.CharField(max_length=200, verbose_name='参数2'),
        ),
        migrations.AlterField(
            model_name='add_web_testcase',
            name='webtestlocation',
            field=models.CharField(max_length=200, verbose_name='定位路径'),
        ),
    ]