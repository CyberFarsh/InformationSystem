from django.shortcuts import render
from .models import AuthUser, Initiative, InitiativeUser
from .forms import initiative


def save_initiative(request):
    form = initiative(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'Altai/CreateInitiative.html', context)


def home(request):
    return render(request, 'Altai/home.html')
