from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from utils import param
from django.core import validators
# Create your models here.
type_choice = (('ch', '教师'), ('admin', '管理员'), ('back', '后勤人员'))
gender_choice = ((1, '女'), (2, '男'))


class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name='姓名')
    pinx = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True, blank=True)
    secode = models.CharField(max_length=5, null=True, blank=True)
    subject = models.CharField(max_length=20, null=True, blank=True, choices=param.get_subject(), verbose_name='科目')
    type = models.CharField(max_length=50, choices=type_choice)
    gender = models.SmallIntegerField(choices=gender_choice)
    graduate = models.CharField(max_length=100)
    school = models.CharField(max_length=100, null=True, blank=True)
    note = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = '教师'
        constraints = [models.UniqueConstraint(fields=['name', 'subject'], name='unique_teacher')]


class TeacherImport(models.Model):
    file = models.FileField(upload_to='excel', validators=[validators.FileExtensionValidator(['xls', 'xlsx'], message='必须为excel文件，后缀名为xls,xlsx!')])


@receiver(pre_delete, sender=TeacherImport)
def teacher_import_delete(sender, instance, **kwargs):
    instance.file.delete(True)
