from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def login_user(request):
    return render(request,'authentication/base.html')


def logout_user(request):
    return render(request,'authentication/base.html')


def register_user(request):
    return render(request,'authentication/base.html')
