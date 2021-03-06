# Generated by Django 3.1.4 on 2021-01-06 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0003_banji'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='学期标题')),
                ('start', models.DateField(verbose_name='开始日期')),
                ('end', models.DateField(verbose_name='结束日期')),
                ('note', models.CharField(max_length=200)),
            ],
        ),
    ]
