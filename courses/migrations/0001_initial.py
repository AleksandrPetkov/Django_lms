# Generated by Django 4.1.5 on 2023-02-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('course_type', models.CharField(db_column='c_type', max_length=20, verbose_name='Course type')),
                ('lessons_number', models.PositiveIntegerField(db_column='lessons', default=16)),
                ('course_program', models.TextField(blank=True, db_column='c_progr', null=True)),
            ],
            options={
                'db_table': 'courses',
            },
        ),
    ]
