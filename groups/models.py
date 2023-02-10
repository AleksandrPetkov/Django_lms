import datetime
import random

from django.db import models
from faker import Faker

from groups.validators import validate_start_date


class Group(models.Model):
    group_name = models.CharField(
        max_length=30,
        verbose_name='Group name',
        db_column='gr_name'
    )
    group_start = models.DateField(default=datetime.date.today, validators=[validate_start_date])
    group_description = models.TextField(null=True, blank=True, db_column='gr_descr')

    class Meta:
        db_table = 'groups'


    @classmethod
    def generate_fake_data(cls, cnt):
        groups_name = ['Java', 'Python', 'PHP']
        for _ in range(cnt):
            s = cls()
            s.group_name = f'{random.choice(groups_name)}'
            s.save()
