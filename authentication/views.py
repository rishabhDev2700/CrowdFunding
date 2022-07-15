from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from authentication.models import CustomUser


def login_user(request):
    url = CustomUser.get()
    return render(request,'base.html')


def logout_user(request):
    return render(request,'base.html')


def register_user(request):
    return render(request,'base.html')
