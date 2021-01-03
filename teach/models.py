from django.db import models

# Create your models here.


class TeachArrange(models.Model):
    title = models.CharField(max_length=50)