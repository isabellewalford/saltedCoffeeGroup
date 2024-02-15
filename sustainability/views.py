from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Sustainability index")

def login(request):
    return HttpResponse("login")

def leaderboard(request):
    return HttpResponse("leaderboard")

def user(request):
    return HttpResponse("user account")

def photo(request):
    return HttpResponse("taking photo")

def collection(request):
    return HttpResponse("card collection")