# Generated by Django 3.1.4 on 2021-01-06 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0006_auto_20210106_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='end',
            field=models.DateField(null=True, verbose_name='结束日期'),
        ),
        migrations.AlterField(
            model_name='term',
            name='start',
            field=models.DateField(null=True, verbose_name='开始日期'),
        ),
    ]
