from django.shortcuts import render
import psycopg2
from .models import AuthUser, Initiative, InitiativeUser
from .forms import initiative


# def create_initiative(request):
#     form_name = name_initiative()
#     form_budget = budget_initiative()
#     form_type = type_initiative()
#     if 'querycard' in request.GET: #fixme
#         form_name = name_initiative(request.GET)
#         name = form_name.cleaned_data['querycard']



def home(request):
    return render(request, 'Altai/home.html')
