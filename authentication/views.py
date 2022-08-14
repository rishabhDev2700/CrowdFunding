from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from authentication.forms import CustomUserCreationForm, UserProfileForm
from authentication.models import UserProfile


def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Successfully Logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials',extra_tags="danger")
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
        messages.info(request, 'Invalid data')
    form = CustomUserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})


@login_required
def update_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        profile = UserProfileForm(request.POST,instance=profile)
        if profile.is_valid():
            profile.save()
            messages.success(request, "Updated Profile")
            return redirect('dashboard')
        else:
            messages.error(request,'Unexpected Error', extra_tags='danger')
            return redirect('profile form')
    form = UserProfileForm(instance=profile)
    return render(request, 'authentication/profile_form.html', context={'form': form})
