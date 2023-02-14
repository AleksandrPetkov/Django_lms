import datetime
import random

from django.db import models
from faker import Faker

from core.models import BaseModel
from core.validators import validate_start_date
from teachers.models import Teacher


class Group(BaseModel):
    group_name = models.CharField(
        max_length=30,
        verbose_name='Group name',
        db_column='gr_name'
    )
    group_start = models.DateField(default=datetime.date.today, validators=[validate_start_date])
    group_description = models.TextField(null=True, blank=True, db_column='gr_descr')
    headman = models.OneToOneField(
        'students.Student', on_delete=models.SET_NULL, null=True, blank=True, related_name='headman_group'
    )
    course = models.OneToOneField(
        'courses.Course', on_delete=models.SET_NULL, null=True, blank=True, related_name='course_group'
    )
    teachers = models.ManyToManyField(to=Teacher, blank=True, related_name='groups')

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'{self.group_name}'

    @classmethod
    def generate_fake_data(cls, cnt):
        groups_name = ['Java', 'Python', 'PHP', 'C#']
        for _ in range(cnt):
            s = cls()
            s.group_name = f'{random.choice(groups_name)}'
            s.save()
