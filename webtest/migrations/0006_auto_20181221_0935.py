# Generated by Django 2.1.1 on 2018-12-21 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0005_webcasestep_webtestlocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webcasestep',
            name='webtestlocation',
            field=models.CharField(choices=[('id', '0'), ('1', 'xpath'), ('2', 'css'), ('3', '图片'), ('4', 'name'), ('5', 'link'), ('6', 'classname'), ('7', 'tagname')], default='0', max_length=200, verbose_name='定位方式'),
        ),
    ]