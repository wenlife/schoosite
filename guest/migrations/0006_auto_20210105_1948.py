# Generated by Django 3.1.4 on 2021-01-05 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0005_auto_20210105_1738'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='teacher',
            constraint=models.UniqueConstraint(fields=('name', 'subject'), name='unique_teacher'),
        ),
    ]
