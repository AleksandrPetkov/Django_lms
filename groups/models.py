from django.db import models

from groups.validators import validate_start_date


class Group(models.Model):
    group_name = models.CharField(
        max_length=30,
        verbose_name='Group name',
        db_column='gr_name'
    )
    group_start = models.DateField(validators=[validate_start_date])
    group_description = models.TextField(null=True, blank=True, db_column='gr_descr')

    class Meta:
        db_table = 'groups'
