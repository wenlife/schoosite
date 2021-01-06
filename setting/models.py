from django.db import models
from django.core import validators
from django import forms
# Create your models here.


class Department(models.Model):
    title = models.CharField(max_length=50)
    entry_year = models.CharField(max_length=4)
    person_in_charge = models.CharField(max_length=40)
    note = models.CharField(max_length=100, null=True, blank=True)


class Banji(models.Model):
    title = models.CharField(max_length=200)
    grade = models.CharField(max_length=4)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    serial = models.SmallIntegerField()
    type = models.CharField(max_length=10)
    school = models.CharField(max_length=100, null=True, blank=True)
    note = models.CharField(max_length=200, null=True, blank=True)


class Term(models.Model):
    title = models.CharField(max_length=200, verbose_name='学期标题')
    start = models.DateField(verbose_name='开始日期')
    end = models.DateField(verbose_name='结束日期')
    note = models.CharField(max_length=200, null=True, blank=True)

