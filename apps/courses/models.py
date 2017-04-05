from __future__ import unicode_literals
from django.db import models

from ..manager.models import Student


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length = 1000)
    students = models.ManyToManyField(Student, related_name="my_course", null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
