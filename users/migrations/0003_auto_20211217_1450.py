# Generated by Django 3.2.9 on 2021-12-17 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211214_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='user_id',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='user_id',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user_id',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
