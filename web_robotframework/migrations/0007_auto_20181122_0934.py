# Generated by Django 2.1.1 on 2018-11-22 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_robotframework', '0006_auto_20181121_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit_case_step',
            name='Webcase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web_robotframework.add_web_name'),
        ),
    ]
