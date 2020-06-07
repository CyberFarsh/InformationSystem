from django.shortcuts import render, redirect
from .models import AuthUser, Initiative, InitiativeUser
from django.contrib.auth import logout as auth
from django.contrib.auth.decorators import login_required
from .special_func import get_next_url
from .forms import initiative


# def save_initiative(request):
#     form = initiative(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context = {'form': form}
#     return render(request, 'Altai/CreateInitiative.html', context)


def home(request):
    return render(request, 'Altai/home.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect(get_next_url(request))
