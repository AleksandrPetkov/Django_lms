import datetime
from random import choice, randint

from dateutil.relativedelta import relativedelta
from django.db import models
from faker import Faker

from core.models import PersonModel
# from core.validators import validate_unique_email
from groups.models import Group


class Student(PersonModel):
    phone = models.CharField(max_length=25) #, null=True
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')

    class Meta:
        db_table = 'students'

    def __str__(self):
        if self.group:
            return f'{self.first_name} {self.last_name}({self.group.group_name})'
        else:
            return f'{self.first_name} {self.last_name}()'


    @classmethod
    def _generate(cls):
        student = super()._generate()
        f = Faker()
        group = Group.objects.all()
        student.phone = f'{f.country_calling_code()}{f.msisdn()[6:]}'
        student.group = choice(group)
        student.save()
