# Generated by Django 3.2.9 on 2021-12-23 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='read_quiz',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
