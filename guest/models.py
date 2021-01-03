from django.db import models
from utils import param
# Create your models here.
type_choice = (('ch', '教师'), ('admin', '管理员'), ('back', '后勤人员'))
gender_choice = ((1, '女'), (2, '男'))


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    pinx = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True, blank=True)
    secode = models.CharField(max_length=5, null=True, blank=True)
    subject = models.CharField(max_length=20, null=True, blank=True, choices=param.get_subject())
    type = models.CharField(max_length=50, choices=type_choice)
    gender = models.SmallIntegerField(choices=gender_choice)
    graduate = models.CharField(max_length=100)
    school = models.CharField(max_length=100, null=True, blank=True)
    note = models.CharField(max_length=200, null=True, blank=True)


class TeacherImport(models.Model):
    file = models.FileField(upload_to='excel')

