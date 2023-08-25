from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy


def login_view(request):
    return render(request, 'app_auth/login.html', {"error": "Пользователь не найден"})


def profile_view(request):
    return render(request, 'app_auth/profile.html')



def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

