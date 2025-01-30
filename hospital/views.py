from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import HttpResponse

def home_page(request):
    return render(request,"home.html")