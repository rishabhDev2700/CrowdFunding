from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(max_length=200, default="")
    occupation = models.CharField(max_length=50, default="")
    picture = models.ImageField(upload_to='users/%Y/%m', blank=True)
    contact = models.CharField(max_length=12, blank=True)
    loaction = models.TextField(max_length=100, blank=True)
