# Generated by Django 4.1.5 on 2023-02-27 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_teacher_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='group',
        ),
    ]