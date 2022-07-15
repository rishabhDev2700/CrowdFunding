from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from authentication.forms import CustomUserCreationForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return reverse('dashboard')
    return render(request, 'authentication/login.html')


def logout_user(request):
    logout(request)
    return render(request, 'authentication/login.html')


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'authentication/login.html')
    form = CustomUserCreationForm()
    return render(request, 'base.html', {'form': form})
