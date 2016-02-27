from django.shortcuts import render
from django.http import HttpResponse
from rango.models import *
from django.contrib.auth.decorators import login_required

def bienvenue(request):
    return render(request, 'base.html')

@login_required
def profile(request):

    return render(request, 'registration/login.html')
