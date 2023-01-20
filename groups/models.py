from django.db import models


class Group(models.Model):
    group_name = models.CharField(
        max_length=30,
        verbose_name='Group name',
        db_column='gr_name'
    )
    group_start = models.DateField()
    group_description = models.TextField(null=True, blank=True, db_column='gr_descr')

    class Meta:
        db_table = 'groups'
