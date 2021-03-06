# Generated by Django 3.1.4 on 2021-01-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0006_auto_20210105_1948'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': '教师'},
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=50, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(blank=True, choices=[('yw', '语文'), ('ds', '数学'), ('yy', '英语'), ('xx', '信息'), ('ty', '体育')], max_length=20, null=True, verbose_name='科目'),
        ),
    ]
