from django.db import models

# Create your models here.
from authentication.models import CustomUser


class Project(models.Model):
    title = models.CharField(max_length=50,blank=False)
    description = models.TextField(max_length=200,blank=False)
    target = models.IntegerField(blank=False)
    goals = models.TextField(max_length=200,blank=False)
    owner = models.ForeignKey(to=CustomUser,on_delete=models.DO_NOTHING)