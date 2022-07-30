from django.db import models
from authentication.models import UserProfile
from user_dashboard.models import Project


class Contribution(models.Model):
    _Currencies = [
        ('INR', 'INR'),
        ('USD', 'USD'),
    ]
    user_id = models.IntegerField(null=False)
    project = models.IntegerField(null=False)
    amount = models.IntegerField(default=50)
    currency = models.CharField(choices=_Currencies, max_length=10, default=_Currencies[0][0])
    payment_id = models.CharField(max_length=22, default='')
    order_id = models.CharField(max_length=24)
    verification_signature = models.CharField(max_length=100, default='')
    verification_status = models.BooleanField(default=False)
    objects = models.Manager()
