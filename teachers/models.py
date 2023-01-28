import datetime

from django.db import models
from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name='First name',
        db_column='f_name'
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Last name',
        db_column='l_name'
    )
    birthday = models.DateField(default=datetime.date.today)
    salary = models.PositiveIntegerField(default=6000)


    class Meta:
        db_table = 'teachers'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()
        for _ in range(cnt):
            s = cls()
            s.first_name = f.first_name()
            s.last_name = f.last_name()
            s.birthday = f.date_between(start_date='-65y', end_date='-18y')
            s.salary = f.random_int(min=6000, max=50000)
            s.save()
