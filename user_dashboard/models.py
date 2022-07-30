from django.db import models
from authentication.models import CustomUser


class Project(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=200, blank=False)
    target = models.IntegerField(blank=False)
    goals = models.TextField(max_length=200, blank=False)
    owner = models.OneToOneField(to=CustomUser, on_delete=models.DO_NOTHING)
    objects = models.Manager()

    def __str__(self):
        return f'Title:{self.title}, target:{self.target}, owner:{self.owner}'
