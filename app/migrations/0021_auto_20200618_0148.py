# Generated by Django 2.2.1 on 2020-06-17 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_settings_loginuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='status',
            field=models.CharField(blank=True, choices=[('D', '未开始'), ('R', '运行中'), ('W', '完成'), ('S', '失败')], default='D', max_length=10, verbose_name='状态'),
        ),
    ]
