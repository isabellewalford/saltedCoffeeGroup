from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

import sustainability.permissions
from sustainability.forms import SignUpForm, PlantOfTheDayForm
from sustainability.models import PlantOfTheDay
from sustainability.permissions import ADD_PLANT_OF_THE_DAY


@login_required()
def home(request):
    try:
        current_plant = PlantOfTheDay.objects.get(date=timezone.now().date())
    except PlantOfTheDay.DoesNotExist:
        current_plant = None
    return render(request, 'sustainability/index.html', {'current_plant': current_plant})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password"
            messages.error(request, error_message)
            return render(request, "registration/login.html")
    else:
        return render(request, "registration/login.html")


@login_required()
def logout_view(request):
    logout(request)
    return redirect('home')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required()
@permission_required('sustainability.add_plant_of_the_day', raise_exception=True)
def plant_of_the_day_view(request):
    if request.method == 'POST':
        form = PlantOfTheDayForm(request.POST)
        if form.is_valid():
            plant_of_the_day = form.save(commit=False)
            plant_of_the_day.added_by = request.user
            plant_of_the_day.save()
            return redirect('home')
        return redirect('plant_of_the_day_view')
    else:
        form = PlantOfTheDayForm()
        try:
            current_plant = PlantOfTheDay.objects.get(date=timezone.now().date())
        except PlantOfTheDay.DoesNotExist:
            current_plant = "Not selected"
    return render(request, 'sustainability/add_plant_of_the_day.html', {'form': form, 'current_plant': current_plant})

@login_required()
def account_view(request):
    return render(request, 'sustainability/user.html')


@login_required()
def leaderboard_view(request):
    return render(request, 'sustainability/leaderboard.html')