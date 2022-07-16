from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from authentication.forms import CustomUserCreationForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Successfully Logged in')
            return render(request, 'base.html')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'authentication/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully Logged out')
    return redirect('login')


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('login')
        messages.info(request,'Invalid data')
    form = CustomUserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})
