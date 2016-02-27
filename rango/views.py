from django.shortcuts import render
from django.http import HttpResponse
from rango.models import *

def bienvenue(request):
    return render(request, 'index.html')