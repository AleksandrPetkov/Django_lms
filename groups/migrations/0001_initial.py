# Generated by Django 4.1.5 on 2023-02-14 11:40

import core.validators
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('group_name', models.CharField(db_column='gr_name', max_length=30, verbose_name='Group name')),
                ('group_start', models.DateField(default=datetime.date.today, validators=[core.validators.validate_start_date])),
                ('group_description', models.TextField(blank=True, db_column='gr_descr', null=True)),
                ('course', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_group', to='courses.course')),
            ],
            options={
                'db_table': 'groups',
            },
        ),
    ]
