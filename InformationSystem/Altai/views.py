from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth
from .special_func import get_next_url


def home(request):
    return render(request, 'Altai/home.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect(get_next_url(request))
