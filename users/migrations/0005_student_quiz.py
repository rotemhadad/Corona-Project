# Generated by Django 3.2.9 on 2021-12-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_student_read_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='quiz',
            field=models.ManyToManyField(default=None, to='users.quiz'),
        ),
    ]
