# Generated by Django 3.2 on 2022-11-17 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_task_status_alter_task_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='创造时间/Create time')),
                ('content', models.CharField(max_length=5000, verbose_name='创作内容/Create Content')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.userinfo', verbose_name='作者/Author')),
            ],
        ),
    ]
