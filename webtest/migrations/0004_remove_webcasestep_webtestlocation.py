# Generated by Django 2.1.1 on 2018-12-20 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0003_auto_20181219_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webcasestep',
            name='webtestlocation',
        ),
    ]