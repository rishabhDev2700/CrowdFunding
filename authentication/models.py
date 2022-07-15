from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    def __str__(self):
        return f'Username: {self.username}, Email: {self.email}'


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(max_length=200, default="")
    occupation = models.CharField(max_length=50, default="")
    picture = models.ImageField(upload_to='users/%Y/%m', blank=True)
    contact = models.CharField(max_length=12, blank=True)
    location = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.user
