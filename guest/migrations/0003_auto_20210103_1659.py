# Generated by Django 3.1.4 on 2021-01-03 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0002_auto_20210103_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, '女'), (2, '男')]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(blank=True, choices=[('yw', '语文'), ('ds', '数学'), ('yy', '英语'), ('xx', '信息')], max_length=20, null=True),
        ),
    ]
