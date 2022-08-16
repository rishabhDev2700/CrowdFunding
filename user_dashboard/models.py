from email.mime import image
from django.db import models
from authentication.models import CustomUser


class Project(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=200, blank=False)
    cover = models.ImageField(upload_to='projects/', blank=True)
    target = models.IntegerField(blank=False)
    goals = models.TextField(max_length=200, blank=False)
    raised = models.IntegerField(default=0)
    owner = models.ForeignKey(to=CustomUser, on_delete=models.DO_NOTHING)
    objects = models.Manager()

    def __str__(self):
        return f'Title:{self.title}, target:{self.target}, owner:{self.owner}'