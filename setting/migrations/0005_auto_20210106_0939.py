# Generated by Django 3.1.4 on 2021-01-06 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0004_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
