from django.db.models import Q
from django.shortcuts import render



def login(request):
    return render(request,"login.html")


def home(request):
    return render(request,"home.html")


def passportverification(request):
    return render(request,"passportverification.html")

def contact(request):
    return render(request,"contact.html")

def tourist(request):
    return render(request,"tourist.html")

def workvisa(request):
    return render(request,"workvisa.html")

def visarenewal(request):
    return render(request,"visarenewal.html")

def studentvisa(request):
    return render(request,"studentvisa.html")



