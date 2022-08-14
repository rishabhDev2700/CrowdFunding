from django.db import models

from authentication.models import UserProfile
from user_dashboard.models import Project


class Contribution(models.Model):
    _Currencies = [
        ('INR', 'INR'),
        ('USD', 'USD'),
    ]
    user = models.ForeignKey(to=UserProfile, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(to=Project, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(default=50)
    currency = models.CharField(choices=_Currencies, max_length=10, default=_Currencies[0][0])
    payment_id = models.CharField(max_length=22, default='')
    order_id = models.CharField(max_length=24)
    verification_signature = models.CharField(max_length=100, default='')
    verification_status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
