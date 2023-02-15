import datetime
import random

from django.db import models
from faker import Faker

from core.models import BaseModel
from groups.models import Group
from teachers.models import Teacher


class Course(BaseModel):
    course_type = models.CharField(max_length= 20, verbose_name='Course type', db_column='c_type')
    lessons_number = models.PositiveIntegerField(default=16, db_column='lessons')
    course_program = models.TextField(null=True, blank=True, db_column='c_progr')

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return f'{self.course_type}'

    @classmethod
    def generate_fake_data(cls, cnt):
        course_name = ['Basic', 'Advanced']
        for _ in range(cnt):
            s = cls()
            s.course_type = f'{random.choice(course_name)}'
            s.save()
