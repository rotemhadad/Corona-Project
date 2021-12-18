# Generated by Django 3.2.9 on 2021-12-18 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211218_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='massege_student',
            name='author_Manager',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.manager'),
        ),
        migrations.AlterField(
            model_name='massege_student',
            name='author_Teacher',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.teacher'),
        ),
    ]
