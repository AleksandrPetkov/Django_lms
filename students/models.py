import datetime

from django.db import models
from faker import Faker

from students.validators import validate_unique_email

VALID_DOMAINS = ('gmail.com', 'yahoo.com', 'test.com')


class Student(models.Model):
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
    age = models.PositiveIntegerField()
    birthday = models.DateField(default=datetime.date.today)
    city = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(validators=[validate_unique_email])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    
    class Meta:
        db_table = 'students'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()
        for _ in range(cnt):
            s = cls()  # s = Student()
            s.first_name = f.first_name()
            s.last_name = f.last_name()
            s.email = f'{s.first_name}.{s.last_name}@{f.random.choice(VALID_DOMAINS)}'
            s.birthday = f.date_between(start_date='-65y', end_date='-18y')
            s.age = f.random_int(min=18, max=65)
            s.save()


